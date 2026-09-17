"""power-hunter CLI — scan SEC filings for equipment-slot arbitrage opportunities.

    python -m power_hunter.cli scan                 # live EDGAR sweep, ranked
    python -m power_hunter.cli scan --query '"SGT6-5000F"' --forms 8-K
    python -m power_hunter.cli demo                 # offline: score sample text, no network

Bulk/long scans belong on GCP (gcp-run), not local Mac RAM — see README.
"""
from __future__ import annotations
import argparse
import json
import sys

from .config import EQUIPMENT_QUERIES, DEFAULT_FORMS
from .ingest import sec_edgar
from .score.arbitrage import build_opportunity, rank


def _scan(args) -> int:
    queries = [args.query] if args.query else EQUIPMENT_QUERIES
    forms = args.forms.split(",") if args.forms else DEFAULT_FORMS
    seen: dict[str, object] = {}
    for q in queries:
        try:
            hits = sec_edgar.search(q, forms=forms, date_from=args.since, limit=args.limit)
        except Exception as e:  # network/UA/rate errors surface honestly, don't fake data
            print(f"[warn] query {q!r} failed: {e}", file=sys.stderr)
            continue
        for f in hits:
            opp = build_opportunity(f, text=f.snippet)
            prev = seen.get(f.accession)
            if prev is None or opp.score > prev.score:
                seen[f.accession] = opp
    ranked = rank(list(seen.values()))
    print(f"# {len(ranked)} ranked opportunities from {len(queries)} queries\n")
    for o in ranked[: args.top]:
        f = o.filing
        print(f"[{o.score:5.1f}] {f.entity}  {f.form} {f.filed}  {f.accession}")
        print(f"        {o.rationale}")
        if f.url:
            print(f"        {f.url}")
    if args.json:
        print(json.dumps([o.to_dict() for o in ranked], default=str, indent=1))
    return 0


def _demo(args) -> int:
    from .models import Filing
    sample = ("The Company disclosed substantial doubt about its ability to continue as a "
              "going concern. Its equipment financing facility includes undelivered gas "
              "turbine (SGT6-5000F) positions with progress payments made, 3 units, ~1.5 GW, "
              "subject to assumption and assignment under section 365.")
    f = Filing(accession="0000000-00-000000", form="10-Q", filed="2026-08-14", entity="DEMO Corp")
    o = build_opportunity(f, text=sample)
    print(json.dumps(o.to_dict(), default=str, indent=1))
    print(f"\nscore={o.score}  ->  {o.rationale}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="power-hunter", description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="live EDGAR sweep")
    s.add_argument("--query"); s.add_argument("--forms")
    s.add_argument("--since", help="YYYY-MM-DD")
    s.add_argument("--limit", type=int, default=30)
    s.add_argument("--top", type=int, default=25)
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=_scan)
    d = sub.add_parser("demo", help="offline scoring demo (no network)")
    d.set_defaults(func=_demo)
    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

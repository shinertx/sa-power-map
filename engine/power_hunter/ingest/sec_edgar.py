"""SEC EDGAR full-text search (EFTS) ingestion — live, zero-dependency (urllib).

EFTS indexes filing bodies 2001-present. This is the real sourcing front door:
query for equipment/distress phrases, get back filing hits to extract + score.
Respects SEC's UA + rate-limit requirements.
"""
from __future__ import annotations
import json
import time
import urllib.parse
import urllib.request

from ..config import SEC_EFTS_URL, SEC_UA, SEC_RATE_LIMIT_PER_SEC, DEFAULT_FORMS
from ..models import Filing

_last_call = [0.0]


def _throttle() -> None:
    gap = 1.0 / SEC_RATE_LIMIT_PER_SEC
    dt = time.time() - _last_call[0]
    if dt < gap:
        time.sleep(gap - dt)
    _last_call[0] = time.time()


def search(query: str, forms=None, date_from=None, date_to=None, limit=50) -> list[Filing]:
    """Run one EFTS query, return Filing objects. Live network call."""
    forms = forms or DEFAULT_FORMS
    params = {"q": query, "forms": ",".join(forms)}
    if date_from:
        params["dateRange"] = "custom"
        params["startdt"] = date_from
        params["enddt"] = date_to or date_from
    url = SEC_EFTS_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": SEC_UA, "Accept": "application/json"})
    _throttle()
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)

    out: list[Filing] = []
    for hit in data.get("hits", {}).get("hits", []):
        src = hit.get("_source", {}) or {}
        adsh = src.get("adsh") or (hit.get("_id") or "").split(":")[0]
        names = src.get("display_names") or []
        entity = names[0] if names else ""
        # display_name form: "Fermi Inc.  (FRMI)  (CIK 0002071778)"
        if "(CIK " in entity:
            entity = entity.split(" (CIK")[0].strip()
        ciks = src.get("ciks") or []
        cik = ciks[0] if ciks else None
        form = src.get("form") or (src.get("root_forms") or [""])[0]
        acc_nodash = (adsh or "").replace("-", "")
        cik_num = (cik or "").lstrip("0")
        url_f = (
            f"https://www.sec.gov/Archives/edgar/data/{cik_num}/{acc_nodash}/{adsh}-index.htm"
            if cik_num and adsh else None
        )
        out.append(Filing(
            accession=adsh or "",
            form=form,
            filed=src.get("file_date", ""),
            entity=entity,
            cik=cik,
            url=url_f,
            snippet=" ".join((src.get("file_description") or "").split())[:400],
        ))
        if len(out) >= limit:
            break
    return out

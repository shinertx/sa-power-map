# power-hunter — equipment-slot arbitrage engine (rebuilt 2026-09-17)

Zero-dependency Python rebuild of the original engine that was lost when the GCP VM
was repurposed. Rebuilt from `../PROJECT.md` + `../deals/VERIFIED_BOOK.md`, refocused on
the real edge: **long-lead equipment and factory-slot positions, not sites.**

## The thesis it serves

AI-datacenter power demand is exploding; new grid connections take years and gas
turbines / large transformers have 2–4 year lead times. Distressed companies and
bankrupt miners hold **undelivered equipment orders and factory slots** they can't use.
Find those holders in SEC filings + §365 dockets, acquire/novate the position cheap,
reassign it to a buyer who'd otherwise wait years. The **undelivered / factory-slot**
position is the prize; the site is backdrop.

## What works now (v1)

- **Ingest** — live SEC EDGAR full-text search (`ingest/sec_edgar.py`), zero-dep urllib,
  UA + rate-limit compliant. Proven: re-surfaces Fermi (FRMI) + Hallador (HNRG).
- **Extract** — equipment/slot + distress + §365 signals from text (`extract/equipment.py`).
- **Score** — equipment-slot arbitrage scoring, prioritising undelivered × distressed ×
  §365 × lead-time (`score/arbitrage.py`).
- **CLI** — `python -m power_hunter.cli scan|demo`.
- **Tests** — `python3 tests/test_extract.py` (5/5 pass, no network).

## Run

```bash
export POWER_HUNTER_UA="Sovereign Power research <you@example.com>"   # SEC requires a contact UA
python -m power_hunter.cli demo                       # offline scoring proof
python -m power_hunter.cli scan --query '"SGT6-5000F"' --forms 8-K,10-Q,10-K
python3 tests/test_extract.py                         # tests
```

## Roadmap (not yet rebuilt)

1. **Deep scoring** — EFTS returns a short description, not the filing body. Add a
   fetch step: pull the filing HTML from `Filing.url` and score the full text (this is
   the original M2). Until then, `scan` ranks on thin snippets.
2. **§365 docket sweep** — CourtListener/RECAP for bankruptcy equipment-assumption motions.
3. **Deal packaging** — regenerate the SPV-option / novation / teaser templates (M3).
4. **Persistence + report** — SQLite book + a static local viewer (replaces the dead VDR).

## Scale / cost note

Per the workspace Heavy-Compute Offload rule, a **bulk** multi-query historical sweep
runs on GCP via `gcp-run`, not local Mac RAM. Single queries (like the smoke test) are
fine locally. No secrets live in this repo; set the UA via env var.

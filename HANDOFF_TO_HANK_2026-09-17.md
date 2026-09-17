# Handoff to Hank — 2026-09-17

From: a Ben-directed Claude Code session (separate from Hank). Ben asked me to capture what I
learned and hand Sovereign Power back to you. **This session is stepping out; you own it.**
One-time note, not a tracker — the live operating doc remains your `SOVEREIGN_POWER_BRIEF.md` v2.

## What I added to the repo

- **`engine/`** — a zero-dependency rebuild of the lost sourcing engine, aligned to your v2
  methodology (equipment/slot first, §365 focus, documentary discipline):
  - `ingest/sec_edgar.py` — live SEC EDGAR full-text search (urllib, UA + rate-limit compliant). Proven live.
  - `extract/equipment.py` — equipment-class + undelivered/factory-slot + distress + §365 signals.
  - `score/arbitrage.py` — scores undelivered × distressed × §365 × lead-time.
  - `cli.py` (`scan`, `demo`), `tests/test_extract.py` (5/5 pass, no network), `README.md`.
  - Use it or ignore it — it's a tool, it asserts no positions.
- **Highest-value next build (roadmap #1):** deep-fetch. EFTS returns only a short description,
  so `scan` currently ranks on thin snippets. Add a step that fetches the filing body from
  `Filing.url` and scores full text — that's what turns it into a real §365/equipment hunter.

## Integrity flags for you (things I verified this session)

1. **`data/equipment_hunter.db` holds the synthetic rows you flagged** (duplicate serials,
   invented LLCs, no CIKs). The engine does NOT depend on it — `demo` uses a hardcoded sample.
   Recommend you treat that DB as untrusted / regenerate it from verified sources only.
2. **The portal is dead.** The VM (`meme-snipe-v19-vm-recovery`, ephemeral IP now 34.75.34.141)
   web root serves an unrelated "William R. Kincaid" biography site; all Sovereign paths 404;
   no Sovereign HTML remains on disk.
3. **The original engine is unrecoverable** — not on the VM, not in `~/teamwork_projects`, no
   GCP snapshot, never on GitHub. `engine/` is a fresh rebuild from `PROJECT.md`, NOT the original.
4. **Backup state:** this repo (`shinertx/sovereign-power`, private) is the only backup. Your v2
   brief was merged intact — I verified I did not clobber it; v1 is preserved in git history.

## Boundaries respected

- No outreach of any kind to any counterparty (Kenisky / Neal Cobb / Sutherland untouched).
- No sends, options, money, or signatures. Nothing external.

## Coordination

Two agents (this session + you) pushed to this repo concurrently today and nearly collided on a
push. Going forward, **you are the single operator.** If Ben wants engine work, he'll route it
to you or open a fresh session that coordinates through this repo — not a parallel pusher.

# Sovereign Power — Operating Brief (v2, 2026-09-17)

**Supersedes** the 2026-09-15 Claude consolidation of 25 Antigravity chats (preserved in git
history). This version is the **live operating document** — it directs daily machine work, not
just records history.

Claims are tagged **[in-docs]** (verified in this repo's own files), **[from-chats]** (stated in
chats, not independently re-verified), **[verified-2026-09-17]** (confirmed by Hank's Sep 17
research cycles), or **[killed]** (investigated and rejected).

---

## 1. What Sovereign is (corrected thesis)

Sovereign buys **time-to-power**: exclusive control of scarce power assets from motivated
sellers, verified against real documents, repositioned to buyers facing multi-year waits. The
asset is enforceable control over a faster path to electricity — not cheap land, not a lead list.

**Equipment and factory-slot positions are the preferred lane** — gas turbines, large
transformers, switchgear, and purchase-order / delivery-slot positions for gear that is ordered
but not yet delivered. A 2–4 year factory queue is the scarce asset; novating a dead project's
equipment order (or buying never-installed hardware out of a §365 process) is the arbitrage.
This lane has the deepest moat because sourcing is buried in bankruptcy dockets, UCC filings,
and 10-Q exhibits — not headlines.

**Disappeared industrial load is the second lane** — shuttered plants with owned, energized
infrastructure (refineries, chlor-alkali, smelters, mills, mines). Sites are the backdrop, not
the prize: energized land is commoditized and contested (MARA, Riot, Soluna, PE funds all hunt
it); you get outbid and the moat is thin.

**The binding constraint is the counterparty, not the asset class.** An exclusive option needs
a motivated seller — a trustee, lender, estate, or distressed owner who wants out. Healthy-owner
rationalizations (real MW, no willing seller) are not positions. **The machine hunts willing
counterparties first, megawatts second.**

Operating funnel: **leads → document-verified positions → exclusive control → buyer LOI → closing.**

Proof target (Ben's bar): one site under control + written confirmation of ≥5 MW deliverable
within 12 months + one qualified buyer LOI.

---

## 2. Book status — RESET 2026-09-17 [verified-2026-09-17]

**Zero verified positions.** Everything below was killed in the Sep 17 research cycles:

- **Mawson / Big Digital Energy (BGDE)** [killed]: the "~129 MW" was crypto-mining load on
  *leased* sites (Midland leased, Bellefonte leased) — not a transferable interconnection right.
  Renamed to Big Digital Energy Inc., ticker BGDE, effective 2026-04-24; new management is
  monetizing its own AI/HPC assets and engaged Northland Capital Markets. Distress is real
  (Aug 14, 2026 Q2 filing) but distress ≠ transferable control. Track as comp only.
- **All four claimed equipment positions** [killed]: GE LM6000 packages, 345 kV / 525 kV
  transformer positions, the "300 MVA March 2027" slot pitched to Neal Cobb, and the "~650
  reroutable positions" — synthetic rows in `data/equipment_hunter.db` (duplicate serial
  numbers across rows, invented LLCs with no CIKs and no state of incorporation); the repo's
  own VERIFIED_BOOK already retired them as illustrations.
- **Legacy ~8 packaged positions**: under re-screening against the documentary gate (§3).
  Cipher Mining (CIFR) flagged first — crypto miner, suspected leased-load trap.

**Live pipeline (unverified, under active diligence):**
- LyondellBasell Houston refinery — closed Q1 2025, LYB owns the 700-acre site, est. 100–250 MW
  former load. Verifiable via 10-K cogen disclosures + ERCOT meter data. Healthy owner planning
  its own reuse — no motivated seller.
- Olin Freeport chlor-alkali shutdown + Dow Freeport PO unit (end 2025) — est. ~100–125 MW
  disappeared load, owned sites. Healthy owners; load may already be reallocated on-site.
- Danskammer HoldCo Ch. 11 (D. Del. 26-10950, 532 MW NYISO gas peaker) — tracked comp only;
  no §363 sale motion filed as of ~Sep 11, 2026. Generation-asset trade, not the load thesis.

**Never again cite as verified:** "1,523 verified assets / 246.8 GW" (that was the indexed filing
universe, not controlled assets); uninstalled LM6000 packages; any 345 kV / 525 kV transformer
position; the 300 MVA March 2027 slot; any industrial load figure as transferable capacity.

---

## 3. The documentary gate — a position enters the book ONLY with these

1. Actual utility service agreement or interconnection record — or a named, obtainable path to it.
2. Meter / load history for the site.
3. Ownership and site-control evidence — **OWNED, not leased.** Leased load is an automatic kill.
4. Assignability and consent requirements identified (utility, landlord, RTO/ISO).
5. For equipment: the actual contract / PO, specs, remaining payments, the named seller in
   control, and a plausible manufacturer-novation path.
6. Written utility or manufacturer confirmation where obtainable.

**Kill rules (fast, no second chances):**
- Leased load presented as transferable capacity (the Mawson trap).
- Synthetic or unverifiable rows — duplicate serials, invented entities, no primary document.
- Healthy-owner rationalization with no motivated seller.
- Pre-FID "cancellations" where no long-lead equipment was ever ordered (nothing to novate).
- Public auctions — zero proprietary edge (Northvolt lesson).
- Terminated-not-novated contracts (Hornsea 4 lesson).
- Wrong asset class: offshore-wind turbines, battery-manufacturing gear, electrolyzers.

---

## 4. Sourcing methodology — what the machine hunts

1. **§365 docket sweep (primary equipment hunt):** live Chapter 11 estates (2024–2026) holding
   executory equipment purchase orders — transformers, turbines, switchgear — with named
   debtors. The US Magnesium docket is the model for surfacing real electrical assets this way.
2. **Disappeared-load hunt:** EIA-860 retirements, plant-closure news, owner-announced shutdowns
   → ERCOT / utility settlement-meter data → motivated-seller check (trustee, lender, estate
   outranks healthy owner).
3. **Comps tracked, not targeted:** Danskammer §363 process, BGDE self-monetization, Fermi
   turbine deployment.

Texas / ERCOT first per Ben's original spec (5 MW+ single site, usable in 6–12 months,
options/exclusivity over speculative purchase).

---

## 5. Standing orders from Ben — do not reinterpret

- **No outreach of any kind** — no sends, replies, forwards, or drafts — to any counterparty
  without Ben's explicit word. Specifically:
  - **Anthony Kenisky**: never respond unless Ben reverses the instruction.
  - **Neal Cobb** (`neal@cobbtx.com`): pitch sent 2026-08-26 (300 MVA transformer claim, now
    killed); no reply found.
  - **Dub Sutherland** (King & Spalding): full Kenisky thread forwarded 2026-09-17 with no
    covering note; no reply found. His role — legal cover vs. deal flow — is unclarified and
    needs Ben.
- Ben says a buyer exists; **no buyer LOI, term sheet, or written commitment was found** in the
  searched accounts. Do not describe any buyer as verified until identified and evidenced.
- No money, no options, no commitments, no signatures without Ben.
- Report to Ben **only on material change**: a newly verified position, a killed flagship, a
  filing that moves a tracked name, or a decision that needs him. Quiet otherwise.

---

## 6. Operating cadence

Daily CEO work cycle — **06:00 CT, 30-minute focused sessions** — attacking the highest-value
constraint in this order: **(1)** a verified position, **(2)** a real buyer with a written
commitment, **(3)** clean outreach threads. Sessions log to the goal workspace and stay silent
unless something material changes. (Scheduler: `sovereign-ceo-work-cycle`.)

---

## 7. Provenance

- **v1 (2026-09-15):** Claude consolidation of 25 Antigravity chats + `PROJECT.md` +
  `MAWSON_PRICING_MEMO.md`. Preserved in git history.
- **v2 (2026-09-17):** Hank operating rewrite at Ben's direction — corrected thesis
  (equipment-first, counterparty-first), book reset to zero, documentary gate, kill rules,
  standing orders. Grounded in the Sep 17 email-verification sweep, the Mawson kill-check, and
  two CEO research cycles (load + equipment).

---
*This brief is the live operating document for the Sovereign project. It directs daily machine
work. It asserts nothing as sent, signed, or verified beyond the tags above.*

# Sovereign Power — Consolidated Brief

**Prepared 2026-09-15 by Claude, consolidating 25 Antigravity chats into this folder.**
Sources: the 25 Antigravity conversation DBs under `~/.gemini/antigravity/conversations/`
that name "Sovereign Power" / "Mawson", plus the two docs already in this folder
(`PROJECT.md`, `MAWSON_PRICING_MEMO.md`). Claims are tagged **[in-docs]** (verified in this
folder's own files), **[from-chats]** (stated in the Antigravity chats, not independently
re-verified), or **[unverified]** (asserted somewhere but contradicted or unconfirmed).
No Codex source exists — the Codex archive has zero Sovereign Power content.

---

## 1. What Sovereign Power is

An autonomous **stranded-power / "time-to-power" arbitrage engine**: it mines public filings
(SEC EDGAR 8-K/10-Q/10-K + Chapter 11, EIA-860/923, EPA FRS/Title V) to find distressed or
shuttered industrial sites that still hold **energized high-voltage grid interconnections**,
then packages **contingent acquisition options** to resell to time-motivated hyperscalers /
AI-compute operators. The value is not the failing business — it's the interconnection +
utility relationships + energized site, because a new large-load grid connection in a
constrained market (esp. PJM) takes years. [in-docs]

Public-facing framing/brand in the chats: **"SOVEREIGN // Infrastructure Arbitrage Desk."**
Operating entity for outreach and signing: **Jockey VC / "Sovereign Infrastructure," ben@jockeyvc.com.** [from-chats]

## 2. Where everything actually lives

| Asset | Location | Notes |
|---|---|---|
| Canonical local folder | `~/Projects/Sovereign Power` (this folder) | Moved here from `~/Documents/Sovereign Power` (~Sep 4) — the old path is deleted; any chat still pointing there is stale |
| Engineering spec | `PROJECT.md` (this folder) | Full "power-hunter" architecture, M1–M5 milestones |
| Live-deal memo | `MAWSON_PRICING_MEMO.md` (this folder) | Disciplined, source-tagged Mawson pricing/structure |
| Code engine(s) | GCP VM `35.237.153.98`: `/home/benjijmac/power-hunter/` and `/home/benjijmac/equipment-hunter/deals/` | The deal packages are generated under `equipment-hunter/deals/` |
| Web terminal / VDR | `http://35.237.153.98/` and `/deals/` | Map terminal indexing the asset database |
| Antigravity workspace | was `~/Documents/antigravity/busy-nobel` | **Gone** — that codename dir no longer exists (current codenames differ) |
| Source chats | 25 DBs in `~/.gemini/antigravity/conversations/` | Top: `82391234…`, `76bfe85c…`, `31fe95d1…` (last is a *different* project — see §6) |

## 3. Asset count — UNRECONCILED, do not cite a single number

Three different asset/deal counts appear across versions: **605**, **1,527**, and **1,762**
indexed assets. [unverified — they conflict] The web terminal title in the latest chat says
1,762; `PROJECT.md` says 1,527; the earlier registry said 605. Treat the count as
**"~hundreds to ~1,700, unreconciled"** until the live DB on the VM is queried directly.

## 4. Lead live deal — Mawson (NASDAQ: MIGI)

Fully worked in `MAWSON_PRICING_MEMO.md`. In one line: ~129 MW across PJM sites (Midland/
Bellefonte PA), stated going-concern doubt, expiring Dec-2026 power hedge → a distressed
seller of energized interconnections. Proposed play: a **120-day purchase option with
assignment rights**, option fee ~$250–500k, strike ~$450–700/kW of *verified firm MW*,
priced only after utility diligence. #1 kill risk: the "129 MW" may be mining load, not firm
utility capacity. [in-docs] All numbers there are individually tagged VERIFIED/REPORTED/SCENARIO.

## 5. Deal-packaging artifacts on the VM (status: drafted, delivery unverified)

The engine generated deal packages under `equipment-hunter/deals/`: multiple
`PKG-*_novation_agreement.md` and `PKG-*_spv_option.md`, an `AUDIT_DOSSIER_VERIFIED.md`, an
`AUTONOMOUS_POWER_TIME_ARBITRAGE_FEASIBILITY_REPORT.md`, and outreach drafted to a
counterparty referred to as **"Neal"** (`EXECUTIVE_ONE_PAGER_NEAL.md`, `EMAIL_TO_NEAL_E2E_MATH.md`).
[from-chats] Who "Neal" is, and whether any email was actually sent, is **not established** in
the chats — do not assume outreach happened. Any send/signature is approval-gated (Jockey entity, Ben's explicit sign-off).

## 6. Precision flags (things not to get wrong)

- **The "$50M/month" figures are NOT Sovereign Power.** One of the 25 chats (`31fe95d1…`) is a
  separate "master-vault cash-cow discovery" swarm that mentions Mawson only in passing; its
  $50M/mo run-rate targets belong to that project, not this one.
- The asset count is unreconciled (§3).
- "605 verified deals" (from the old rogue registries) is the least-supported figure — the
  live terminal shows a larger, different number.
- The Antigravity `busy-nobel` workspace and the old `~/Documents/Sovereign Power` path are
  both gone; this folder + the VM are the only live homes.

## 7. Open loops / next proofs (unstarted — for whoever picks this up)

1. SSH the VM (`35.237.153.98`) and query the live asset DB to settle the real count and pull
   the current deal pipeline — the terminal is the source of truth, not any doc.
2. Confirm whether the "Neal" outreach was ever sent (and who Neal is) before drafting more.
3. Mawson: the whole memo hinges on the utility interconnection/service agreements — that
   document set is the single highest-leverage diligence item.
4. Reconcile this brief's pointers into the registry entry `sovereign_power`
   (`~/Projects/Sovereign Power` is already its canonical_path).

---
*This brief consolidates chat history into durable form; it is not a valuation opinion and
asserts nothing as sent, signed, or verified beyond the tags above.*

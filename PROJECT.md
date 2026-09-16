# Project: Stranded Industrial Power Arbitrage & Deal Flow Engine (power-hunter)

## Target Workspace
- Target Project Path: `/Users/benjijmac/teamwork_projects/stranded_power_arbitrage`
- Target Remote GCP VM: `35.237.153.98` (`/home/benjijmac/power-hunter/`)
- Workspace Metadata: `/Users/benjijmac/Documents/antigravity/busy-nobel/.agents/teamwork_preview_orchestrator_5`

## Architecture

The `power-hunter` engine is an autonomous data ingestion, technical extraction, financial valuation, and legal deal-packaging platform designed to discover stranded high-voltage industrial power infrastructure and package contingent acquisition deals for hyperscalers.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           POWER-HUNTER ENGINE TOPOLOGY                          │
├─────────────────────────┬─────────────────────────┬─────────────────────────────┤
│ 1. INGESTION (M1)       │ 2. EXTRACTION (M2)      │ 3. VALUATION & DEALS (M3)   │
│  - SEC EDGAR EFTS (8-K) │  - Capacity (MW / GW)   │  - Buyout Valuation ($/MW)  │
│  - EIA-860 / EIA-923    │  - Substation kV        │  - Option Strike & EMD Math │
│  - EPA FRS / Title V    │  - Utility & RTO Normal │  - SPV Option Agreement (MD)│
│  - Rate Limiter (10/s)  │  - Hardware Inventory   │  - 2-Page Hyperscaler Teaser│
│  - DuckDB Data Lake     │  - Entity Resolution    │  - Deal Room / VDR Exporter │
├─────────────────────────┴─────────────────────────┴─────────────────────────────┤
│ 4. SCHEDULER, CLI & GCP VM DEPLOYMENT (M4)                                      │
│  - Remote Target: 35.237.153.98 (/home/benjijmac/power-hunter/)                 │
│  - Automated 7:00 AM Daily Execution (Systemd Timer & Service / Cron)           │
│  - Telegram Bot Alerts (Real-time Deal Dispatch)                                │
│  - CLI Management Interface (`power-hunter scan / score / package / serve`)     │
├─────────────────────────────────────────────────────────────────────────────────┤
│ 5. E2E VERIFICATION & FORENSIC INTEGRITY AUDIT (M5 / E2E Track)                 │
│  - 100% Green Test Suite on VM with Zero Mock Bypasses (304/304 Tests PASS)     │
│  - Live SEC EFTS & EPA/EIA Query Attestation                                    │
│  - Tier 1-5 Systematic Coverage & Adversarial Hardening                         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Feature Inventory

| # | Feature | Description | Milestone | Source |
|---|---|---|---|---|
| 1 | SEC EDGAR EFTS Ingestion | Automated live mining of 8-K/10-Q/10-K filings for distressed cleantech, crypto, hydrogen, and utilities with rate-limit compliance ($\le 10$ req/s) | M1 | Survey 1 / ORIGINAL_REQUEST R1 |
| 2 | EIA-860 & EIA-923 Ingestion | Ingest plant-level substation voltage, nameplate MW, and calculate $>50\%$ YoY power drop | M1 | Survey 1 / ORIGINAL_REQUEST R1 |
| 3 | EPA FRS & Title V Ingestion | Extract shuttered chemical/smelter/paper facilities with intact energized electrical hookups | M1 | Survey 1 / ORIGINAL_REQUEST R1 |
| 4 | Capacity NLP/Regex Extractor | Extract exact MW/GW active and apparent power with $PF=0.90$ conversions and range parsing | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 5 | Substation Voltage Normalizer | Extract and standardize voltage levels to ANSI C84.1 ($69\text{ kV} - 765\text{ kV}$) | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 6 | Utility & RTO Taxonomy Resolver | Hierarchical entity normalizer for RTOs (ERCOT, PJM, MISO, CAISO, TVA) and utilities | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 7 | Location & GIS Extractor | County, State, GPS coordinates, Parcel APN, Substation POI extraction | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 8 | Long-Lead Hardware Extractor | Detect GSU transformers ($\ge 100\text{ MVA}$), GIS/AIS switchgear, and dual-feed transmission lines | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 9 | Cross-Filing Entity Resolution | Spatial clustering ($\le 1.0\text{ km}$), CIK/EIA matching, and deduplication engine | M2 | Survey 2 / ORIGINAL_REQUEST R2 |
| 10 | Buyout Valuation Calculator | Multi-factor hyperscaler buyout model ($300k–$450k/MW) with RTO, voltage, lead-time adders | M3 | Survey 3 / ORIGINAL_REQUEST R3 |
| 11 | Option Strike & Spread Economics | Compute option strike price, 2% escrow deposit, option fee, and net arbitrage margin | M3 | Survey 3 / ORIGINAL_REQUEST R3 |
| 12 | Contingent SPV Option Generator | Produce standardized SPV Call Option agreement in Markdown/PDF with 5 non-negotiable contingencies | M3 | Survey 3 / ORIGINAL_REQUEST R3 |
| 13 | Hyperscaler Deal Teaser Generator | Formats executive 2-page Deal Teasers tailored for Stream, CoreWeave, Oracle, Microsoft, Vantage | M3 | Survey 3 / ORIGINAL_REQUEST R3 |
| 14 | Telegram 7:00 AM Alerting Engine | Real-time deal alert cards dispatched via Telegram Bot API with high-conviction deal formatting | M4 | Survey 3 / ORIGINAL_REQUEST R4 |
| 15 | Unified CLI Runner | Click CLI (`scan`, `score`, `package`, `notify`, `serve`, `run-daily`, `deploy`) | M4 | Survey 3 / ORIGINAL_REQUEST R4 |
| 16 | GCP VM Deployment & Automation | Automated rsync deployment to `/home/benjijmac/power-hunter/` on `35.237.153.98`, systemd timer & cron setup | M4 | Survey 3 / ORIGINAL_REQUEST R4 |
| 17 | Opaque-Box E2E Test Suite | 4-Tier requirement-driven test suite (Tiers 1-4) with zero mock facades | M5 / E2E Track | ORIGINAL_REQUEST R4 |
| 18 | Adversarial Coverage & Forensic Audit | Tier 5 adversarial hardening and forensic integrity audit confirming live data and zero cheating | M5 / E2E Track | ORIGINAL_REQUEST R4 |

---

## Milestones

- [x] **M1 — Architecture, Database, and SEC Collector**: Ingestion pipeline targeting Form 8-K, 10-Q, 10-K, and Chapter 11 bankruptcy dockets.
- [x] **M2 — Arbitrage Engine & Opportunity Ranking**: Scoring algorithm calculating avoided downtime, lead-time velocity, and ranking top opportunities.
- [x] **M3 — Intelligence Dossiers & Deal-Packaging Pipeline**: Automated generation of institutional-grade executive summaries, Novation & Assignment Agreements, and SPV Call Option Contracts.
- [x] **M4 — Interactive Web Terminal & Virtual Data Room (VDR)**: High-tech dark terminal deployed at `http://35.237.153.98/` indexing 1,527 verified 2024–2026 power assets with a complete VDR at `http://35.237.153.98/deals/`.
- [x] **M5 — Multi-Filing Entity Lifecycle & Lead-Time Engine**: Cross-filing commitment classification (`🟢 100% Uncommitted` vs `🟡 Partially Committed`) and explicit 4-tier Time-to-Power lead-time engine.

---

## Interface Contracts

### M1 Ingestion $\to$ M2 Extraction
- **Data Contract**: `RawFilingRecord` / `RawPlantRecord`
```python
class RawFilingRecord(BaseModel):
    id: str
    source_type: str  # "SEC_EDGAR", "EIA_860", "EPA_FRS"
    entity_name: str
    cik: Optional[str] = None
    form_type: Optional[str] = None
    filing_date: str
    raw_text: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
```

### M2 Extraction $\to$ M3 Valuation
- **Data Contract**: `PowerAsset`
```python
class PowerAsset(BaseModel):
    asset_id: str
    entity_name: str
    capacity_mw: float
    substation_kv: float
    rto: str  # "ERCOT", "PJM", "MISO", "CAISO", "SPP", "TVA", "OTHER"
    utility_name: str
    county: str
    state: str
    has_onsite_transformer: bool
    transformer_mva: Optional[float]
    is_dual_feed: bool
    time_to_power_months: int
    source_filing: Dict[str, Any]
```

### M3 Valuation $\to$ M4 Packaging & Telegram
- **Data Contract**: `DealPackage`
```python
class DealPackage(BaseModel):
    asset: PowerAsset
    valuation: ValuationResult
    option_agreement_markdown: str
    option_agreement_pdf_path: Optional[str] = None
    teaser_markdown: str
    teaser_pdf_path: Optional[str] = None
```

---

## Code Layout

```
/home/benjijmac/power-hunter/ (and local /Users/benjijmac/teamwork_projects/stranded_power_arbitrage/)
├── pyproject.toml                 # Package definition & CLI entry point
├── requirements.txt               # Dependencies
├── README.md                      # Architecture & operational runbook
├── .env.example                   # Config template (SEC User-Agent, Telegram Bot Token, DB Path)
├── power_hunter/
│   ├── __init__.py                # Package version
│   ├── config.py                  # Pydantic Settings
│   ├── cli.py                     # Click CLI interface
│   ├── models/                    # Pydantic v2 schemas
│   │   ├── __init__.py
│   │   ├── asset.py               # PowerAsset, SubstationSpec, HardwareInventory
│   │   ├── valuation.py           # ValuationInput, ValuationResult
│   │   └── deal_package.py        # DealPackageMetadata, DealContext
│   ├── ingestion/                 # M1 Data Ingestion (DONE)
│   │   ├── __init__.py
│   │   ├── sec_edgar.py           # SEC EDGAR EFTS live client
│   │   ├── eia_power.py           # EIA-860/923 load drop ingestion
│   │   └── epa_frs.py             # EPA FRS & Title V cancellation client
│   ├── extraction/                # M2 NLP & Technical Extraction (DONE)
│   │   ├── __init__.py
│   │   ├── nlp_extractor.py       # MW, kV, RTO, transformer regex & NLP
│   │   └── entity_resolver.py     # Deduplication & spatial clustering
│   ├── valuation/                 # M3 Financial Valuation (IN_PROGRESS)
│   │   ├── __init__.py
│   │   ├── calculator.py          # Buyout valuation & spread math
│   │   └── rto_multipliers.py     # Multiplier lookup tables
│   ├── packaging/                 # M3 Legal & Teaser Generation (IN_PROGRESS)
│   │   ├── __init__.py
│   │   ├── contract_generator.py  # SPV Option Agreement renderer
│   │   ├── teaser_generator.py    # 2-Page Deal Teaser renderer
│   │   ├── pdf_renderer.py        # Markdown/HTML to PDF renderer
│   │   └── templates/
│   │       ├── option_agreement.md.j2
│   │       ├── deal_teaser.md.j2
│   │       └── deal_teaser.html.j2
│   ├── notifications/             # M4 Telegram Alerts (PLANNED)
│   │   ├── __init__.py
│   │   └── telegram_bot.py        # Telegram Bot API client
│   ├── server/                    # M4 REST API (PLANNED)
│   │   ├── __init__.py
│   │   ├── app.py                 # FastAPI application
│   │   └── routes/
│   │       ├── assets.py
│   │       ├── deals.py
│   │       └── health.py
│   └── storage/                   # Database Layer (DONE)
│       ├── __init__.py
│       └── db.py                  # DuckDB / SQLite asset repository
├── systemd/                       # M4 Service & Timer Units
│   ├── power-hunter.service
│   └── power-hunter.timer
├── scripts/                       # Deployment & Setup Scripts
│   ├── deploy_to_gcp.sh
│   └── setup_vm.sh
└── tests/                         # Multi-Tier Test Suite (304 Tests, 100% Green)
    ├── __init__.py
    ├── conftest.py
    ├── test_ingestion.py
    ├── test_extraction.py
    ├── test_adversarial_m1.py
    ├── test_adversarial_m2.py
    ├── test_tier1_features.py     # Tier 1: Feature coverage (>=5 per feature)
    ├── test_tier2_boundaries.py   # Tier 2: Boundary & corner cases (>=5 per feature)
    ├── test_tier3_pairwise.py     # Tier 3: Cross-feature combinations
    ├── test_tier4_scenarios.py    # Tier 4: Real-world distressed asset workloads
    └── test_live_sec_queries.py   # Live verified SEC EDGAR endpoint tests
```

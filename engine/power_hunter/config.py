"""Configuration. No secrets here — override via environment variables.

SEC requires a User-Agent with a real contact. Set POWER_HUNTER_UA before a live run:
    export POWER_HUNTER_UA="Sovereign Power research <you@example.com>"
"""
import os

# SEC EDGAR full-text search (EFTS) — public, no key. Rate-limit: <=10 req/s.
SEC_EFTS_URL = "https://efts.sec.gov/LATEST/search-index"
SEC_UA = os.environ.get("POWER_HUNTER_UA", "Sovereign Power research (set POWER_HUNTER_UA)")
SEC_RATE_LIMIT_PER_SEC = 8

# Forms worth scanning for equipment/distress signals.
DEFAULT_FORMS = ["8-K", "10-Q", "10-K"]

# Equipment/slot search queries — the sourcing edge. Phrases that co-occur with
# distressed holders of long-lead gear.
EQUIPMENT_QUERIES = [
    '"undelivered equipment" turbine',
    '"gas turbine" "going concern"',
    '"SGT6-5000F"',
    '"step-up transformer" "purchase order"',
    '"progress payments" turbine',
    '"section 365" turbine OR transformer',
    '"equipment monetization" liquidity',
]

# Scoring weights.
W_UNDELIVERED = 40      # a factory-slot / PO position is the prize
W_DISTRESS = 25         # motivated seller
W_SECTION_365 = 20      # assignable via bankruptcy
W_LEAD_MONTHS = 0.4     # per month of lead time the buyer avoids
MIN_REPORT_SCORE = 30

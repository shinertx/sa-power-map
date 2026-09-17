"""Core data models for the equipment/slot arbitrage engine.

The thesis: the scarce asset is long-lead POWER EQUIPMENT (gas turbines, large
transformers, switchgear) and undelivered factory-slot / purchase-order positions —
NOT the real-estate site. A distressed holder of that equipment, reachable via SEC
filings and §365 bankruptcy dockets, is the sourcing target.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Optional
import datetime as _dt


@dataclass
class Filing:
    """A raw SEC filing hit from ingestion."""
    accession: str
    form: str            # 8-K, 10-Q, 10-K, etc.
    filed: str           # YYYY-MM-DD
    entity: str
    cik: Optional[str] = None
    url: Optional[str] = None
    snippet: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


# Long-lead equipment classes and their typical lead times (months) — the scarcity
# that creates the arbitrage. Sourced from PROJECT.md / VERIFIED_BOOK observations.
EQUIPMENT_LEAD_MONTHS = {
    "gas_turbine": 42,        # Siemens SGT6-5000F ("F-class"), GE 7F etc.
    "aeroderivative": 18,     # LM6000 / recip gensets — the bridge tech
    "gsu_transformer": 30,    # generator step-up / large power transformers (>=100 MVA)
    "switchgear_gis": 24,     # GIS / AIS high-voltage switchgear
    "interconnect_slot": 48,  # energized interconnection / queue position
}


@dataclass
class EquipmentSignal:
    """An equipment/slot signal extracted from a filing's text."""
    equipment_class: str          # key of EQUIPMENT_LEAD_MONTHS
    matched_text: str             # the phrase that fired
    undelivered: bool = False     # factory-slot / progress-payment position (the prize)
    mw: Optional[float] = None
    lead_months: int = 0


@dataclass
class Opportunity:
    """A scored equipment-slot arbitrage opportunity."""
    filing: Filing
    signals: list[EquipmentSignal] = field(default_factory=list)
    distress: bool = False        # going-concern / Chapter 11 / motivated-seller flag
    section_365: bool = False     # bankruptcy §365 assignable-contract context
    score: float = 0.0
    rationale: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        return d

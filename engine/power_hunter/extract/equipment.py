"""Extract equipment/slot + distress signals from filing text.

Regex/keyword first pass (deterministic, testable). The value is catching the
UNDELIVERED / factory-slot language — that is the novation prize the desk hunts.
"""
from __future__ import annotations
import re
from ..models import EquipmentSignal, EQUIPMENT_LEAD_MONTHS

# equipment_class -> patterns that indicate that class of long-lead gear
_EQUIP_PATTERNS = {
    "gas_turbine": r"\b(gas turbine|combustion turbine|SGT6-?5000F|7F\.0[45]|F-?class|Firebird|heavy[- ]duty turbine|CCGT)\b",
    "aeroderivative": r"\b(LM6000|LM2500|aeroderivative|recip(?:rocating)? (?:engine|genset)|MTU|Wartsila)\b",
    "gsu_transformer": r"\b(step-?up transformer|GSU|power transformer|\d{2,4}\s?MVA transformer|large power transformer)\b",
    "switchgear_gis": r"\b(GIS switchgear|gas-insulated switchgear|AIS switchgear|high[- ]voltage switchgear)\b",
    "interconnect_slot": r"\b(interconnection agreement|interconnect(?:ion)? rights|queue position|energized|firm (?:capacity|MW)|point of interconnection)\b",
}
_UNDELIVERED = re.compile(
    r"\b(undelivered|not yet delivered|progress payment|purchase order|factory slot|"
    r"delivery slot|deposit(?:s)? (?:paid|made)|reservation (?:fee|payment)|on order|to be delivered)\b",
    re.I,
)
_MW = re.compile(r"(\d{2,4}(?:\.\d+)?)\s?(?:MW|megawatts?)\b", re.I)
_DISTRESS = re.compile(
    r"\b(going concern|substantial doubt|chapter 11|bankruptc|debtor-in-possession|"
    r"liquidat|wind[- ]down|impairment|default|forbearance|monetiz\w* .{0,20}liquidity)\b",
    re.I,
)
_SEC365 = re.compile(r"\bsection\s?365\b|\b§\s?365\b|assume and assign|executory contract", re.I)


def extract_signals(text: str) -> list[EquipmentSignal]:
    text = text or ""
    undelivered = bool(_UNDELIVERED.search(text))
    mws = [float(m) for m in _MW.findall(text)]
    max_mw = max(mws) if mws else None
    out: list[EquipmentSignal] = []
    for cls, pat in _EQUIP_PATTERNS.items():
        m = re.search(pat, text, re.I)
        if m:
            out.append(EquipmentSignal(
                equipment_class=cls,
                matched_text=m.group(0),
                undelivered=undelivered,
                mw=max_mw,
                lead_months=EQUIPMENT_LEAD_MONTHS.get(cls, 0),
            ))
    return out


def has_distress(text: str) -> bool:
    return bool(_DISTRESS.search(text or ""))


def has_section_365(text: str) -> bool:
    return bool(_SEC365.search(text or ""))

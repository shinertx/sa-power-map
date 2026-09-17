"""Score equipment-slot arbitrage opportunities.

Higher score = better novation/reassignment target: a distressed holder of an
UNDELIVERED long-lead position, ideally assignable via §365. Lead time avoided is
what a time-desperate AI-datacenter buyer actually pays for.
"""
from __future__ import annotations
from ..models import Filing, Opportunity, EquipmentSignal
from ..extract.equipment import extract_signals, has_distress, has_section_365
from ..config import (
    W_UNDELIVERED, W_DISTRESS, W_SECTION_365, W_LEAD_MONTHS, MIN_REPORT_SCORE,
)


def build_opportunity(filing: Filing, text: str | None = None) -> Opportunity:
    text = text if text is not None else (filing.snippet or "")
    signals = extract_signals(text)
    distress = has_distress(text)
    s365 = has_section_365(text)

    score = 0.0
    reasons = []
    if signals:
        best_lead = max(s.lead_months for s in signals)
        score += best_lead * W_LEAD_MONTHS
        reasons.append(f"{len(signals)} equipment signal(s), max lead {best_lead}mo")
        if any(s.undelivered for s in signals):
            score += W_UNDELIVERED
            reasons.append("UNDELIVERED/factory-slot position (novation prize)")
    if distress:
        score += W_DISTRESS
        reasons.append("distress/going-concern")
    if s365:
        score += W_SECTION_365
        reasons.append("§365 assignable context")

    return Opportunity(
        filing=filing, signals=signals, distress=distress, section_365=s365,
        score=round(score, 1), rationale="; ".join(reasons) or "no equipment/distress signal",
    )


def rank(opportunities: list[Opportunity], min_score: float = MIN_REPORT_SCORE) -> list[Opportunity]:
    keep = [o for o in opportunities if o.score >= min_score]
    return sorted(keep, key=lambda o: o.score, reverse=True)

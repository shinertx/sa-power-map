"""Deterministic tests for extraction + scoring — no network."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from power_hunter.extract.equipment import extract_signals, has_distress, has_section_365
from power_hunter.score.arbitrage import build_opportunity, rank
from power_hunter.models import Filing


TURBINE = ("undelivered gas turbine SGT6-5000F positions with progress payments made, "
           "3 units ~1500 MW, subject to assumption and assignment under section 365; "
           "substantial doubt about going concern.")


def test_equipment_signal_detected():
    sigs = extract_signals(TURBINE)
    classes = {s.equipment_class for s in sigs}
    assert "gas_turbine" in classes
    assert any(s.undelivered for s in sigs), "undelivered/factory-slot must be flagged"


def test_distress_and_365():
    assert has_distress(TURBINE)
    assert has_section_365(TURBINE)


def test_mw_extracted():
    sigs = extract_signals(TURBINE)
    assert any(s.mw == 1500 for s in sigs)


def test_scoring_prioritises_undelivered_distressed():
    hot = build_opportunity(Filing("a", "10-Q", "2026-08-14", "Hot Co"), text=TURBINE)
    cold = build_opportunity(Filing("b", "10-K", "2026-01-01", "Cold Co"),
                             text="We operate a gas turbine plant. Normal operations.")
    assert hot.score > cold.score
    assert hot.score >= 30
    ranked = rank([cold, hot])
    assert ranked and ranked[0].filing.entity == "Hot Co"


def test_no_false_positive_on_empty():
    o = build_opportunity(Filing("c", "8-K", "2026-01-01", "Empty"), text="")
    assert o.score == 0.0 and not o.signals


if __name__ == "__main__":
    import traceback
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    passed = 0
    for fn in fns:
        try:
            fn(); passed += 1; print(f"PASS {fn.__name__}")
        except Exception:
            print(f"FAIL {fn.__name__}"); traceback.print_exc()
    print(f"\n{passed}/{len(fns)} passed")
    raise SystemExit(0 if passed == len(fns) else 1)

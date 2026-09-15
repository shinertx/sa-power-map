"""Verification and integrity test suite for Sovereign Power Workspace Isolation & Mirroring (Milestone 1)."""

import os
import sqlite3
import urllib.request
import json
import pytest

SOVEREIGN_POWER_ROOT = "/Users/benjijmac/Documents/Sovereign Power"
BUSY_NOBEL_ROOT = "/Users/benjijmac/Documents/antigravity/busy-nobel"
REMOTE_VM_IP = "35.237.153.98"

EXPECTED_REPORTS = [
    "VERIFIED_BOOK.md",
    "DOE_TITLE_17_EIR_PRE_APPLICATION_BRIEF.md",
    "EXECUTIVE_ONE_PAGER_NEAL.md",
    "EMAIL_TO_NEAL_E2E_MATH.md",
    "AUTONOMOUS_POWER_TIME_ARBITRAGE_FEASIBILITY_REPORT.md",
    "AUDIT_DOSSIER_VERIFIED.md",
]

EXPECTED_PKG_IDS = [
    "PKG-09dc2a91",
    "PKG-2d621031",
    "PKG-88b7e470",
    "PKG-aa1202a9",
    "PKG-d67cc36e",
    "PKG-d8398b4d",
    "PKG-e6ed9b6c",
    "PKG-ed0e3fd6",
]

EXPECTED_PKG_SUFFIXES = [
    "_novation_agreement.md",
    "_spv_option.md",
    "_teaser.html",
    "_teaser.pdf",
]


@pytest.mark.parametrize("root_path", [SOVEREIGN_POWER_ROOT, BUSY_NOBEL_ROOT])
def test_deals_directory_strategic_reports(root_path):
    """Verify all 6 verified strategic reports exist and are non-empty in deals/."""
    deals_dir = os.path.join(root_path, "deals")
    assert os.path.isdir(deals_dir), f"Missing deals directory in {root_path}"

    for report in EXPECTED_REPORTS:
        report_path = os.path.join(deals_dir, report)
        assert os.path.isfile(report_path), f"Missing report: {report_path}"
        file_size = os.path.getsize(report_path)
        assert file_size > 500, f"Report {report} in {root_path} is suspiciously small: {file_size} bytes"


@pytest.mark.parametrize("root_path", [SOVEREIGN_POWER_ROOT, BUSY_NOBEL_ROOT])
def test_strategic_reports_key_content_anchors(root_path):
    """Verify substantive content markers in strategic reports."""
    deals_dir = os.path.join(root_path, "deals")

    with open(os.path.join(deals_dir, "VERIFIED_BOOK.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "THE VERIFIED BOOK" in content
        assert "605" in content or "264.8 GW" in content or "Danskammer" in content

    with open(os.path.join(deals_dir, "DOE_TITLE_17_EIR_PRE_APPLICATION_BRIEF.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "Section 1706" in content
        assert "Title 17" in content

    with open(os.path.join(deals_dir, "EXECUTIVE_ONE_PAGER_NEAL.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "MEMORANDUM: ORPHANED PROGRESS & TEMPORAL POWER ARBITRAGE" in content
        assert "neal@equityx.com" in content

    with open(os.path.join(deals_dir, "EMAIL_TO_NEAL_E2E_MATH.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "TEMPORAL POWER ARBITRAGE" in content
        assert "300 MVA" in content

    with open(os.path.join(deals_dir, "AUTONOMOUS_POWER_TIME_ARBITRAGE_FEASIBILITY_REPORT.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "Autonomous Power Infrastructure Time-Arbitrage" in content
        assert "Executive Summary" in content

    with open(os.path.join(deals_dir, "AUDIT_DOSSIER_VERIFIED.md"), "r", encoding="utf-8") as f:
        content = f.read()
        assert "LIVE POWER REALITY AUDIT" in content
        assert "SEC EDGAR" in content


@pytest.mark.parametrize("root_path", [SOVEREIGN_POWER_ROOT, BUSY_NOBEL_ROOT])
def test_deal_packages_count_and_types(root_path):
    """Verify all 32 deal package files (8 pkgs x 4 files) exist in deals/."""
    deals_dir = os.path.join(root_path, "deals")
    
    for pkg_id in EXPECTED_PKG_IDS:
        for suffix in EXPECTED_PKG_SUFFIXES:
            filename = f"{pkg_id}{suffix}"
            pkg_path = os.path.join(deals_dir, filename)
            assert os.path.isfile(pkg_path), f"Missing deal package file: {pkg_path}"
            assert os.path.getsize(pkg_path) > 0, f"Empty package file: {pkg_path}"

    all_files = [f for f in os.listdir(deals_dir) if not f.startswith(".")]
    assert len(all_files) == 38, f"Expected 38 files (6 reports + 32 pkgs) in {deals_dir}, found {len(all_files)}"


@pytest.mark.parametrize("root_path", [SOVEREIGN_POWER_ROOT, BUSY_NOBEL_ROOT])
def test_equipment_hunter_sqlite_database(root_path):
    """Verify SQLite equipment database integrity and table counts."""
    db_path = os.path.join(root_path, "data", "equipment_hunter.db")
    assert os.path.isfile(db_path), f"Database not found at {db_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check integrity
    cursor.execute("PRAGMA integrity_check;")
    status = cursor.fetchone()
    assert status and status[0] == "ok", f"Database integrity check failed: {status}"

    # Verify tables
    expected_tables = {
        "entities": 8,
        "filings": 8,
        "equipment_assets": 8,
        "arbitrage_opportunities": 8,
        "valuations": 11,
        "deal_packages": 8,
    }

    for table, expected_min_rows in expected_tables.items():
        cursor.execute(f"SELECT count(*) FROM {table};")
        row_count = cursor.fetchone()[0]
        assert row_count >= expected_min_rows, f"Table {table} in {db_path} has {row_count} rows, expected >= {expected_min_rows}"

    conn.close()


def test_busy_nobel_quarantine_isolation():
    """Verify non-power contamination is moved out of busy-nobel root and into _quarantine."""
    root_entries = set(os.listdir(BUSY_NOBEL_ROOT))

    # Forbidden directories/files in active root
    forbidden_items = ["openclaw", "companies", "systemd", "scripts"]
    for item in forbidden_items:
        assert item not in root_entries, f"Contaminant '{item}' should not be in busy-nobel root"

    # Verify _quarantine exists and contains quarantined components
    quarantine_dir = os.path.join(BUSY_NOBEL_ROOT, "_quarantine")
    assert os.path.isdir(quarantine_dir), "_quarantine directory missing in busy-nobel"

    quarantine_entries = set(os.listdir(quarantine_dir))
    assert "openclaw" in quarantine_entries, "openclaw missing from _quarantine"
    assert "companies" in quarantine_entries, "companies missing from _quarantine"
    assert "systemd" in quarantine_entries, "systemd missing from _quarantine"
    assert "scripts" in quarantine_entries, "scripts missing from _quarantine"


@pytest.mark.parametrize("root_path", [SOVEREIGN_POWER_ROOT, BUSY_NOBEL_ROOT])
def test_gemini_master_guide_anchoring(root_path):
    """Verify GEMINI.md exists, is non-empty, and contains Sovereign Power Master Guide directives."""
    gemini_path = os.path.join(root_path, "GEMINI.md")
    assert os.path.isfile(gemini_path), f"GEMINI.md missing in {root_path}"

    with open(gemini_path, "r", encoding="utf-8") as f:
        content = f.read()
        assert "SOVEREIGN // Project Master Guide" in content
        assert "Zero-Hallucination Invariant" in content
        assert "35.237.153.98" in content
        assert "VERIFIED_BOOK.md" in content


def test_remote_gcp_vm_live_endpoints():
    """Verify live connectivity and data feed on remote GCP VM."""
    # Test Caddy root
    req = urllib.request.Request(f"http://{REMOTE_VM_IP}/", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        assert resp.status == 200

    # Test all_positions.json
    req = urllib.request.Request(f"http://{REMOTE_VM_IP}/all_positions.json", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        assert resp.status == 200
        data = json.loads(resp.read().decode("utf-8"))
        assert isinstance(data, list)
        assert len(data) >= 1500, f"Expected >= 1500 assets in feed, got {len(data)}"

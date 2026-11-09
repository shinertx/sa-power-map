#!/usr/bin/env python3
"""
One-command CRM synchronizer for Stage One Power LLC.
Keeps 4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx (Google Sheets / Excel) and
4_STAGE_ONE_MASTER_CRM_303_SITES.md (LLM-readable Markdown) 100% synced.
"""
import openpyxl
from pathlib import Path

BASE = Path("/Users/benjijmac/Projects/Stage One Power")
XLSX_PATH = BASE / "4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx"
MD_PATH = BASE / "4_STAGE_ONE_MASTER_CRM_303_SITES.md"

def export_xlsx_to_md():
    wb = openpyxl.load_workbook(XLSX_PATH, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return
    headers = [str(h or "").replace("\n", " ").strip() for h in rows[0]]
    lines = [
        "# Stage One Power — Single-Page Master CRM (312 Rows: 9 Portfolio + 303 Sites)",
        "",
        "> **Auto-Synced Mirror of `4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx` (`Stage_One_Master_CRM` tab).**",
        "> LLMs (`Muse / Hank`, `Antigravity`, `Google Gemini`) can read this `.md` file directly without parsing binary `.xlsx`.",
        "> Run `python3 sync_crm.py` after any spreadsheet or CSV update to refresh this `.md` mirror.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for r in rows[1:]:
        vals = [str(c if c is not None else "").replace("\n", " ").replace("|", "\\|").strip() for c in r]
        lines.append("| " + " | ".join(vals) + " |")
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Synced {len(rows)-1} CRM rows -> {MD_PATH.name}")

if __name__ == "__main__":
    export_xlsx_to_md()

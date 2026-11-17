#!/usr/bin/env python3
"""
Bidirectional CRM -> Live Map & Markdown Synchronizer for Stage One Power LLC.
Reads edits & new rows from `4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx` (`Stage_One_Master_CRM` tab)
and updates:
  1. `index.html` (`const SITES = ...`)
  2. `3_STAGE_ONE_SAN_ANTONIO_MAP.html` (mirror of `index.html`)
  3. `4_STAGE_ONE_MASTER_CRM_303_SITES.md` (LLM-readable Markdown table)
Automatically geocodes any newly added row that has a Street Address and blank Latitude/Longitude.
"""
import json
import re
import shutil
import urllib.parse
import urllib.request
from pathlib import Path
import openpyxl

BASE = Path(__file__).resolve().parent
XLSX_PATH = BASE / "4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx"
MD_PATH = BASE / "4_STAGE_ONE_MASTER_CRM_303_SITES.md"
INDEX_PATH = BASE / "index.html"
MAP_COPY_PATH = BASE / "3_STAGE_ONE_SAN_ANTONIO_MAP.html"

OUT_REV = {
    "not contacted": "none",
    "contacted": "sent",
    "firm contacted": "firm",
    "replied": "replied",
    "bounced": "bounced",
    "do not contact": "hold",
}

def geocode_address(addr: str, zip_code: str = ""):
    q_str = f"{addr}, {zip_code}, TX".strip(", ")
    q = urllib.parse.urlencode({"SingleLine": q_str, "maxLocations": 1, "f": "json"})
    url = f"https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?{q}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = json.loads(urllib.request.urlopen(req, timeout=10).read().decode("utf-8"))
    cands = data.get("candidates") or []
    if cands:
        loc = cands[0].get("location") or {}
        return round(float(loc["y"]), 6), round(float(loc["x"]), 6)
    return None, None

def to_float(val):
    if val is None or str(val).strip() == "":
        return None
    try:
        return round(float(str(val).replace(",", "").strip()), 2)
    except ValueError:
        return None

def sync_all():
    wb = openpyxl.load_workbook(XLSX_PATH)
    ws = wb["Stage_One_Master_CRM"] if "Stage_One_Master_CRM" in wb.sheetnames else wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return

    headers = [str(h or "").replace("\n", " ").strip() for h in rows[0]]
    col = {h.lower(): idx for idx, h in enumerate(headers)}

    # Load current SITES from index.html so all rich nested fields (au, pm, etc.) are preserved
    html = INDEX_PATH.read_text(encoding="utf-8")
    m = re.search(r"const SITES = (\[.*?\]);\n", html, re.S)
    sites = json.loads(m.group(1)) if m else []
    by_id = {s["id"]: s for s in sites}

    wb_dirty = False
    for r_offset, r in enumerate(rows[1:], start=2):
        raw_id = str(r[col.get("site #", 0)] or "").strip()
        if not raw_id.isdigit():
            continue
        sid = int(raw_id)
        rg_txt = str(r[col.get("region", 1)] or "").lower()
        is_tx = "ercot" in rg_txt or "texas" in rg_txt or sid >= 1000
        pri_txt = str(r[col.get("priority star", 2)] or "").strip().lower()
        sh = 1 if pri_txt in ("yes", "y", "1", "true", "star", "priority") else 0
        gov_col = col.get("government / doe track") if col.get("government / doe track") is not None else col.get("government / public host")
        gov_raw = str(r[gov_col] or "").strip() if gov_col is not None else ""
        gov_l = gov_raw.lower()
        gov_on = 1 if (gov_l.startswith(("yes", "y", "1", "true", "gov", "rule 1")) or "rule 1" in gov_l) else 0
        sci_on = 1 if ("rule 2" in gov_l or "open sci" in gov_l or "research" in gov_l) else 0
        gov_gt = gov_raw.split("—", 1)[1].strip() if ("—" in gov_raw and (gov_on or sci_on)) else ""
        st_txt = str(r[col.get("site status", 3)] or "").strip().lower()
        lo = to_float(r[col.get("mw low", 4)])
        hi = to_float(r[col.get("mw high", 5)])
        if lo is not None and hi is None:
            hi = lo
        if hi is not None and lo is None:
            lo = hi
        out_txt = str(r[col.get("outreach status", 6)] or "").strip().lower()
        o_code = OUT_REV.get(out_txt, "none")

        name = str(r[col.get("property name", 7)] or "").strip()
        addr = str(r[col.get("street address", 8)] or "").strip()
        z = str(r[col.get("zip", 9)] or "").strip()
        ar = str(r[col.get("area / submarket", 10)] or "").strip()
        ct = str(r[col.get("broker / owner contact", 11)] or "").strip()
        em = str(r[col.get("email / website", 12)] or "").strip()
        ph = str(r[col.get("phone", 13)] or "").strip()
        sz = str(r[col.get("building / land size", 14)] or "").strip()
        f_grade = str(r[col.get("fiber grade", 15)] or "?").strip() or "?"
        fl_det = str(r[col.get("fiber detail", 16)] or "").strip()
        notes = str(r[col.get("plain-english notes", 17)] or "").strip()
        la = to_float(r[col.get("latitude", 19)])
        ln = to_float(r[col.get("longitude", 20)])

        if (la is None or ln is None) and addr:
            la, ln = geocode_address(addr, z)
            if la is not None and ln is not None:
                ws.cell(r_offset, col.get("latitude", 19) + 1).value = la
                ws.cell(r_offset, col.get("longitude", 20) + 1).value = ln
                wb_dirty = True
                print(f"Geocoded new row #{sid} ({addr}) -> {la}, {ln}")

        if sid in by_id:
            s = by_id[sid]
            s["sh"] = sh
            if gov_col is not None:
                if gov_on:
                    s["gov"] = 1
                    if gov_gt:
                        s["gt"] = gov_gt
                else:
                    s.pop("gov", None)
                    s.pop("gt", None)
                if sci_on:
                    s["sci"] = 1
                    if gov_gt:
                        s["gt"] = gov_gt
                else:
                    s.pop("sci", None)
            if lo is not None:
                s["lo"] = lo
            if hi is not None:
                s["hi"] = hi
            s["o"] = o_code
            if name:
                s["n"] = name
            if addr:
                s["a"] = addr
            s["z"] = z
            s["ar"] = ar
            s["ct"] = ct
            s["em"] = em
            s["ph"] = ph
            s["sz"] = sz
            s["f"] = f_grade
            s["fl"] = fl_det
            if st_txt == "ruled out":
                s["x"] = notes or "Ruled out in Master CRM"
            else:
                if s.get("x") and st_txt != "ruled out":
                    s["x"] = ""
                if notes:
                    s["sg"] = notes
            if "occupied" in st_txt:
                s["occ"] = 1
            elif "occ" in s and st_txt in ("published power", "validated", "open"):
                del s["occ"]
            if la is not None and ln is not None:
                s["la"] = la
                s["ln"] = ln
        elif la is not None and ln is not None:
            new_s = {
                "id": sid,
                "n": name or addr,
                "a": addr,
                "z": z,
                "ar": ar or ("ERCOT" if is_tx else "San Antonio Region"),
                "t": 1 if (hi or 0) >= 4.5 else 2,
                "c": "Multi-Pod Whales (3–6 Pods)" if (hi or 0) >= 4.5 else "Industrial Parks & Warehouses (1–2 Pods)",
                "la": la,
                "ln": ln,
                "sz": sz,
                "lo": lo,
                "hi": hi,
                "sg": "" if st_txt == "ruled out" else notes,
                "ct": ct,
                "ph": ph,
                "em": em,
                "dc": 1 if (ct or ph or em) else 0,
                "f": f_grade,
                "fl": fl_det,
                "o": o_code,
                "ot": "",
                "v": 0,
                "l": "",
                "vr": 0,
                "sc": 8 if sh else 3,
                "sh": sh,
                **({"gov": 1, "gt": gov_gt or "Government Land"} if gov_on else {}),
                **({"sci": 1} if sci_on else {}),
                **({"gov": 1, "gt": gov_gt or "Government Host"} if gov_on else {}),
                "au": {"p": [notes] if notes else ["Added via Master CRM"], "n": [], "act": "Synced from Master CRM"},
                "x": (notes or "Ruled out in Master CRM") if st_txt == "ruled out" else "",
                "pm": None,
            }
            if is_tx:
                new_s["rg"] = "tx"
            if "occupied" in st_txt:
                new_s["occ"] = 1
            sites.append(new_s)
            by_id[sid] = new_s

    if wb_dirty:
        wb.save(XLSX_PATH)

    if m:
        sites.sort(key=lambda x: (1 if x.get("rg") == "tx" or x["id"] >= 1000 else 0, x["id"]))
        new_json = json.dumps(sites, ensure_ascii=False, separators=(",", ":"))
        html_updated = html[:m.start()] + f"const SITES = {new_json};\n" + html[m.end():]
        INDEX_PATH.write_text(html_updated, encoding="utf-8")
        shutil.copyfile(INDEX_PATH, MAP_COPY_PATH)
        print(f"Synced {len(sites)} sites from Excel -> index.html & 3_STAGE_ONE_SAN_ANTONIO_MAP.html")

    # Export clean Markdown mirror
    rows_fresh = list(ws.iter_rows(values_only=True))
    n_sites = sum(1 for r in rows_fresh[1:] if str(r[0] or "").strip().isdigit())
    lines = [
        f"# Stage One Power — Single-Page Master CRM ({n_sites} Total Sites: San Antonio Region + ERCOT)",
        "",
        "> **Auto-Synced Mirror of `4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx` (`Stage_One_Master_CRM` tab).**",
        "> Edit `4_STAGE_ONE_MASTER_CRM_303_SITES.xlsx` and run `python3 sync_crm.py` to update both the live map (`index.html`) and this `.md` file.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for r in rows_fresh[1:]:
        vals = [str(c if c is not None else "").replace("\n", " ").replace("|", "\\|").strip() for c in r]
        lines.append("| " + " | ".join(vals) + " |")
    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Synced {n_sites} CRM rows -> {MD_PATH.name}")

if __name__ == "__main__":
    sync_all()

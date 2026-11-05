# Design System: Sovereign Institutional CRM & Workbench (`DESIGN.md`)

> **Canonical Source of Truth (Antigravity Global UI Standard)**
> Synthesizes **`shadcn-ui` (`New York` / `Zinc`)**, **`taste-design` (Google Stitch Anti-Slop Standard)**, **`ui-ux-pro-max` (`Sales Intelligence CRM` & `Data-Dense Cockpit`)**, and **`modern-web-guidance`**.
> Applies to all non-JENNi web apps, CRMs, interactive maps, deal rooms, and dashboards (for JENNi surfaces, use `JENNI-DESIGN-SPEC.md`).

---

## 1. Visual Theme & Atmosphere

* **Atmosphere:** High-trust institutional workbench (Attio + Linear + Zillow + Palantir Foundry Light). Clinical, crisp, fast, and zero-fluff.
* **Taste Spectrum Calibration:**
  * **Density:** `7/10` (*Daily-App Balanced to Cockpit-Dense* — high data visibility, compact `8px–12px` grid gaps, zero wasted banner space).
  * **Variance:** `4/10` (*Structured Split-Screen & Asymmetric Workbenches* — never generic 3-equal-card marketing rows).
  * **Motion:** `5/10` (*Fluid Hardware-Accelerated CSS* — `150ms–220ms cubic-bezier(0.16, 1, 0.3, 1)` on `transform` and `opacity` only).
* **Zero-Gate Principle:** Open directly into the working tool, map, and live data table. Never hide the application behind a PIN wall, login screen, or splash brochure.

---

## 2. Color Palette & Functional Roles (`shadcn-ui` Zinc Light Base — Zero Orange/Neon/Rainbow)

Never use dark-mode `#111111` + orange (`#FF5500`) + neon green (`#10B981`) or multi-color rainbow pills. Stick strictly to the calibrated `Zinc` monochrome scale (`#FAFAFA` / `#FFFFFF` / `#09090B`) with clean subtle slate borders (`#E4E4E7`) and understated institutional semantic tokens:

| Descriptive Name | CSS Variable | Hex / Value | Functional Role |
| :--- | :--- | :--- | :--- |
| **Canvas Alabaster** | `--bg-canvas` | `#FAFAFA` (`Zinc-50`) | Primary application background and table header fill |
| **Pure Surface** | `--bg-card` | `#FFFFFF` | Cards, data tables, slide-over sheets, and top navigation bar |
| **Muted Well** | `--bg-muted` | `#F4F4F5` (`Zinc-100`) | Segmented controls, pill tracks, secondary wells, hover states |
| **Active Selection Tint** | `--bg-active` | `#F0F9FF` (`Sky-50`) | Selected card, active table row, or focused deal item |
| **Structural Hairline** | `--border` | `#E4E4E7` (`Zinc-200`) | Default `1px solid` border on cards, tables, inputs, and dividers |
| **Hover Border** | `--border-strong` | `#D4D4D8` (`Zinc-300`) | Hovered input or secondary button border |
| **Obsidian Ink** | `--fg` | `#09090B` (`Zinc-950`) | Primary headings, body copy, and key metrics (never `#000000`) |
| **Graphite Secondary** | `--fg-secondary` | `#3F3F46` (`Zinc-700`) | Table cells, secondary labels, and filter chips |
| **Muted Steel** | `--fg-muted` | `#71717A` (`Zinc-500`) | Captions, address sublines, column headers, and metadata |
| **Subtle Placeholder** | `--fg-subtle` | `#A1A1AA` (`Zinc-400`) | Input placeholders and completed/strikethrough tasks |
| **Institutional Primary** | `--primary` | `#18181B` (`Zinc-900`) | Primary action buttons (`#FAFAFA` text; hover `#27272A`) |
| **Signal Blue Accent** | `--accent` | `#0284C7` (`Sky-600`) | Active selection rings, links, eyebrows, and Tier-1 map pins |
| **Verified Emerald** | `--success` | `#16A34A` (`#DCFCE7` fill) | Verified, Optioned, or Closed-Won status badges and map pins |
| **In-Progress Amber** | `--warning` | `#D97706` (`#FEF3C7` fill) | Walkthrough scheduled, pending diligence, or caution states |
| **Priority Crimson** | `--danger` | `#DC2626` (`#FEE2E2` fill) | Government / Anchor priority targets (`Pod #1`) or critical alerts |

---

## 3. Typography Rules (`taste-design`)

* **Sans-Serif UI & Headings (`--font-sans`):** `'Geist', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif`
  * **App / Section Title:** `20px–28px`, `font-weight: 800`, `letter-spacing: -0.025em`, `line-height: 1.15`.
  * **Card / Sheet Title:** `15px–18px`, `font-weight: 700`, `letter-spacing: -0.015em`.
  * **Body / Table Cell:** `13px–14px`, `font-weight: 400–500`, `line-height: 1.5`.
* **Monospace Data & Eyebrows (`--font-mono`):** `'JetBrains Mono', monospace`
  * **Mandatory Tabular Numerals:** Every number, currency value, MW/kVA figure, phone number, rank ID (`#1`), and keyboard shortcut (`⌘K`) **must** use `font-family: var(--font-mono); font-variant-numeric: tabular-nums;`.
  * **Section Eyebrows:** `11px`, `font-weight: 600`, `text-transform: uppercase`, `letter-spacing: 0.06em`, `color: var(--accent)`.

---

## 4. Component Stylings (`shadcn-ui` New York Spec)

* **Top App Bar (`.topbar`):**
  * Fixed `54px` height, `#FFFFFF` background, `1px solid #E4E4E7` bottom border.
  * Left: Brand monogram badge (`28px × 28px`, `6px` radius, `#18181B` fill) + bold title + concise mono tag.
  * Center: Segmented tab switcher (`.segmented-nav` on `#F4F4F5` track with `#FFFFFF` active pill and live item counts).
  * Right: `Ask AI / Search (⌘K)` trigger + `Showroom Mode` toggle.
* **Buttons (`.btn`):**
  * Height `34px` (`28px` for `.btn-sm`), `padding: 0 12px`, `border-radius: 6px`, `font-size: 13px`, `font-weight: 600`.
  * Tactile active press: `transform: translateY(1px)` over `80ms`. Zero neon outer glows.
* **Cards & List Items (`.card`, `.site-item`):**
  * `#FFFFFF` fill, `1px solid #E4E4E7` border, `8px–12px` radius, subtle shadow `0 1px 2px rgba(9,9,11,0.05)`.
  * Interactive cards lift on hover (`border-color: #0284C7`, `box-shadow: 0 4px 6px -1px rgba(9,9,11,0.07)`).
* **Data Tables (`modern-web-guidance: responsive-table`):**
  * Always wrap `<table>` in `<div class="table-responsive">` (`overflow-x: auto; -webkit-overflow-scrolling: touch;`).
  * Sticky headers (`position: sticky; top: 0; background: #FAFAFA; z-index: 2;`).
  * Prevent wrapping on IDs, metrics, phones, and action buttons (`white-space: nowrap`).
* **Slide-Over Deal Sheet (`.deal-sheet`):**
  * Right-docked `460px` drawer (`transform: translateX(100%)` to `translateX(0)` over `220ms cubic-bezier(0.16, 1, 0.3, 1)`), `-8px 0 30px -4px rgba(9,9,11,0.12)` shadow.
  * Top action bar inside sheet: maximum 2 high-leverage buttons (e.g., `Generate 90-Day Option` + `Copy Broker Script`).
* **Modals & Lightboxes (`modern-web-guidance: light-dismiss-a-dialog`):**
  * Always use native `<dialog closedby="any">` plus a backdrop click listener fallback (`if (e.target === e.currentTarget) e.currentTarget.close()`).

---

## 5. Layout & Interactive Map Principles

* **Split-Screen Map Workbench (`100dvh`):**
  * Left Pane (`500px–540px`): KPI summary strip (`4` compact metric boxes) + Search & Quick-Filter Chip Bar + Scrollable Cards/Table list with a `Cards | Table` view toggle.
  * Right Pane (`flex: 1`): Full-bleed interactive map with floating top-left layer switcher (`Clean Street Map` | `Satellite Parking Lot View` | `Fit All`).
* **Watermark-Free Map Tiles (Mandatory):**
  * Never use `basemaps.cartocdn.com` on public/GitHub Pages domains (it stamps `API KEY REQUIRED` across the map).
  * Use **Esri World Topo / Street Map** (`https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}`) for clean street view and **Esri World Imagery** (`https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}`) for zoom-18 parking lot / transformer inspection.

---

## 6. Anti-Patterns & Pre-Delivery Verification Gate

### Banned Patterns (Never Do)
1. **No Emojis in UI:** Never use emoji characters (`🗺️`, `🎯`, `⚡`, `🏛️`, `🤖`) as icons in navigation, buttons, or headers. Use `1.5px–1.75px` stroke inline Lucide SVGs (`currentColor`).
2. **No Dark-Mode Neon / AI Purple Slop:** Never use glowing cyan/purple gradients, pure `#000000` backgrounds, or low-contrast slate-on-slate text.
3. **No Unverified Field Names (`#undefined`):** Before binding a JSON array to UI templates, inspect `array[0]` in Python/Node to verify exact property names (`rank` vs `id`, `contact` vs `owner`, `size` vs `mw`).
4. **No Fake Metrics:** Every KPI counter and MW/dollar figure must compute dynamically from the real dataset.

### Mandatory Pre-Delivery Verification Checklist (`Exit Code 0`)
- [ ] **JS Syntax Gate:** Run `node -e` with `new Function(scriptContent)` on the extracted `<script>` block to prove **0 syntax errors** before deployment.
- [ ] **No `#undefined` Gate:** Verify every rendered card/row shows real IDs, titles, metrics, and contact numbers.
- [ ] **Live Browser Screenshot Gate:** Open or reload the page in Chrome via `chrome-devtools` MCP, click an item to open its drawer/modal, and take a screenshot (`take_screenshot`) to visually confirm layout, map tiles, and clickability.

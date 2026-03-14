# largest-economies-information-visualization

A reproducible data-preparation and redesign-planning workflow for a Tableau visualization project based on the IMF World Economic Outlook (WEO) dataset. This repository focuses on historical GDP by country from 1980 to 2022 using the IMF indicator `PPPGDP` — GDP at current prices, purchasing power parity, measured in **billions of international dollars**.

The broader goal is to critique and redesign the HowMuch visualization **"Largest Economies in the World Over the Last 40 Years"** using principles from Jonathan Schwabish, Edward Tufte, and Dunford. The repository does **not** claim authorship of the IMF data; it documents a transparent extraction, cleaning, and Tableau-preparation workflow for educational and visualization purposes.

---

## Project overview

The starting point is the IMF WEO Excel export, `data/input/WEOOct2025all.xlsx`, which stores the data in a wide format with one column per year. The script `scripts/extract_weo_pppgdp.py` filters the spreadsheet to the relevant IMF series, keeps the years 1980–2022, and writes a unified top-10 CSV by default for quick Tableau use.

This project supports a redesign assignment built around the original infographic. The documentation in this repository records:

- where the source data came from,
- how the raw IMF spreadsheet was transformed,
- why the redesign strategy changed during evaluation,
- and how the cleaned outputs are meant to be used in Tableau.

---

## Motivation

The original infographic tells an interesting rank-over-time story, but it also overloads that story with too many competing visual elements: dense crossing lines, decorative flags and circular badges, strong region coloring, and evenly spaced time columns despite uneven year intervals. These choices make the chart visually engaging, but they also make it harder to follow individual countries accurately.

The purpose of this repository is to separate **data preparation** from **visual redesign**. By creating a clean, reproducible Tableau-ready dataset, the redesign work can focus on clarity, analytical task, and visual hierarchy rather than spreadsheet wrangling.

---

## Assignment context

This repository supports a course project that requires:

- selecting an existing visualization,
- identifying at least three major issues in priority order,
- citing course readings to justify the critique and redesign,
- creating a redesigned Tableau draft,
- and documenting the process in a Word submission with screenshots.

The final write-up, screenshots, and APA citations are produced outside this repository. This repository serves as the reproducible technical and planning backbone for that work.

---

## Source visualization and data

- **Visualization selected:** *Largest Economies in The World Over the Last 40 Years* (HowMuch)
- **Underlying data used in this repo:** IMF World Economic Outlook (WEO) Excel export
- **Raw source files in repo:**
    - `data/input/WEOOct2025all.xlsx` (primary IMF WEO input)
    - `data/input/Largest Economies in The World Over the Last 40 Years.xlsx` (HowMuch-linked secondary spreadsheet)
- **Indicator used:** `PPPGDP`

Original infographic used as the baseline for critique and redesign:

![Original infographic showing the world's biggest economies over time](original_infographic.jpg)

---

## Indicator used

| IMF code | Full name | Unit |
|---|---|---|
| `PPPGDP` | GDP, current prices, purchasing power parity | Billions of international dollars |

This indicator was chosen because it matches the GDP (PPP) framing of the original visualization and supports cross-country comparison better than nominal GDP measured only in domestic currency.

---

## Repository structure

```text
largest-economies-information-visualization/
├── data/
│   └── input/
│       ├── WEOOct2025all.xlsx
│       └── Largest Economies in The World Over the Last 40 Years.xlsx
├── scripts/
│   ├── extract_weo_pppgdp.py
│   └── convert_howmuch_xlsx.py
├── original_infographic.jpg
├── README.md
├── docs/
│   ├── PROCESS.md
│   ├── READING_PRINCIPLES.md
│   └── private/                    # local-only docs (gitignored)
├── requirements.txt
├── .gitignore
└── output/                         # generated locally by the script
    ├── weo_pppgdp_infographic_years_top10.csv
    └── howmuch_infographic_years_top10.csv
```

---

## How to run the scripts

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run the extraction script from the repository root:

```bash
python scripts/extract_weo_pppgdp.py
```

Default behavior for this script:
- outputs only `output/weo_pppgdp_infographic_years_top10.csv`

To also generate extended outputs (long files and XLSX files), run:

```bash
python scripts/extract_weo_pppgdp.py --all-outputs
```

To convert the HowMuch-linked spreadsheet into the same unified output schema:

```bash
python scripts/convert_howmuch_xlsx.py
```

Default behavior for this script:
- outputs only `output/howmuch_infographic_years_top10.csv`

To also generate extended outputs (XLSX + unified folder files), run:

```bash
python scripts/convert_howmuch_xlsx.py --all-outputs
```

The IMF extraction script will:

1. load the WEO Excel file,
2. filter to the `PPPGDP` indicator and annual observations,
3. keep years 1980–2022,
4. rank countries per year,
5. and save the top-10 benchmark-year output into the `output/` folder.

Both scripts keep the same column schema in their default top-10 CSV outputs, so the two sources can be used together in Tableau without extra reshaping.

---

## Output files

| File | Contents |
|---|---|
| `weo_pppgdp_infographic_years_top10.csv` | Default IMF output (top 10 economies for benchmark years) |
| `howmuch_infographic_years_top10.csv` | Default HowMuch-linked output (top 10 entries parsed from assignment spreadsheet) |
| `weo_pppgdp_1980_2022_long.csv` | Optional (`--all-outputs`) IMF long format |
| `weo_pppgdp_infographic_years_long.csv` | Optional (`--all-outputs`) IMF benchmark-years long format |

**Recommended Tableau starting file:** `weo_pppgdp_infographic_years_top10.csv`

It is focused, immediately available in default mode, and aligned to the benchmark years used in the original infographic.

---

## Output column reference

| Column | Description |
|---|---|
| `country_id` | IMF 3-letter country code |
| `country` | Full country name |
| `indicator_id` | Always `PPPGDP` in the cleaned outputs |
| `indicator` | Full IMF indicator label |
| `scale` | Value scale |
| `unit` | Measurement unit |
| `year` | Calendar year |
| `rank` | Position within year (1 = largest GDP in that source/year) |
| `source_dataset` | Input source identifier |
| `source_vintage` | Data vintage/update context |
| `source_file` | Input file path inside the repository |
| `gdp_ppp_billions_intl_dollars` | GDP (PPP) value in billions of international dollars |

Example rows:

| country_id | country | indicator_id | year | gdp_ppp_billions_intl_dollars |
|---|---|---|---|---|
| USA | United States | PPPGDP | 1980 | 2857.325 |
| JPN | Japan | PPPGDP | 1980 | 1027.574 |
| DEU | Germany | PPPGDP | 1980 | 856.000 |

---

## Tableau use and redesign direction

The cleaned data is intended for Tableau. The current redesign strategy treats:

- **small multiples as the primary redesign direction**, and
- **a simplified bump chart as an exploratory backup**.

This shift happened because a bump chart preserves rank movement well, but for this specific dataset it may still produce too many crossings and too much label congestion even after simplification. Small multiples reduce clutter, eliminate tangled trajectories, and better support a clarity-first redesign.

For the Tableau workflow and redesign rationale, see:

- [`docs/PROCESS.md`](docs/PROCESS.md)
- [`docs/READING_PRINCIPLES.md`](docs/READING_PRINCIPLES.md)

---

## Attribution

**Data source:** International Monetary Fund (IMF), *World Economic Outlook (WEO)* database, October 2025 edition.

**Indicator:** `PPPGDP` — GDP, current prices, purchasing power parity; billions of international dollars.

This repository is intended for educational and visualization-redesign purposes. It documents a reproducible workflow for extracting and reshaping IMF data and does not claim ownership of the underlying values.

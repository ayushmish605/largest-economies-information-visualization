# largest-economies-information-visualization

A reproducible data-preparation and redesign-planning workflow for a Tableau visualization project based on the IMF World Economic Outlook (WEO) dataset. This repository focuses on historical GDP by country from 1980 to 2022 using the IMF indicator `PPPGDP` — GDP at current prices, purchasing power parity, measured in **billions of international dollars**.

The broader goal is to critique and redesign the HowMuch visualization **"Largest Economies in the World Over the Last 40 Years"** using principles from Jonathan Schwabish, Edward Tufte, and Dunford. The repository does **not** claim authorship of the IMF data; it documents a transparent extraction, cleaning, and Tableau-preparation workflow for educational and visualization purposes.

---

## Project overview

The starting point is the IMF WEO Excel export, `data/input/WEOOct2025all.xlsx`, which stores the data in a wide format with one column per year. A single script, `build_largest_economies_data.py`, now processes both inputs and writes one combined top-10 CSV by default for quick Tableau use.

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
├── build_largest_economies_data.py
├── original_infographic.jpg
├── README.md
├── docs/
│   ├── PROCESS.md
│   ├── READING_PRINCIPLES.md
│   ├── SOURCE_METADATA.md
│   └── private/                    # local-only docs (gitignored)
├── requirements.txt
├── .gitignore
└── output/                         # generated locally by the script
    └── largest_economies_top10_combined.csv
```

---

## How to run the script

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the unified script from the repository root:

```bash
python build_largest_economies_data.py
```

Default behavior:
- outputs one file: `output/largest_economies_top10_combined.csv`
- includes both sources in one table via the `source_dataset` column

To also generate extended outputs (source-specific CSVs, long files, and XLSX files), run:

```bash
python build_largest_economies_data.py --all-outputs
```

The unified script will:

1. load both input files,
2. parse and normalize top-10 benchmark-year rows,
3. keep years 1980, 1990, 2000, 2010, 2020, 2021, and 2022,
4. rank by source/year,
5. and save the combined top-10 output into the `output/` folder.

Source file names and vintage details are tracked in metadata docs instead of output columns. See `docs/SOURCE_METADATA.md`.

---

## Output files

| File | Contents |
|---|---|
| `largest_economies_top10_combined.csv` | Default output containing both sources with `source_dataset` |
| `weo_pppgdp_infographic_years_top10.csv` | Optional (`--all-outputs`) IMF-only top 10 output |
| `howmuch_infographic_years_top10.csv` | Optional (`--all-outputs`) HowMuch-linked top 10 output |
| `weo_pppgdp_1980_2022_long.csv` | Optional (`--all-outputs`) IMF long format |
| `weo_pppgdp_infographic_years_long.csv` | Optional (`--all-outputs`) IMF benchmark-years long format |

**Recommended Tableau starting file:** `largest_economies_top10_combined.csv`

It is focused, immediately available in default mode, and lets you compare both sources with one import.

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
- [`docs/SOURCE_METADATA.md`](docs/SOURCE_METADATA.md)

---

## Attribution

**Data source:** International Monetary Fund (IMF), *World Economic Outlook (WEO)* database, October 2025 edition.

**Indicator:** `PPPGDP` — GDP, current prices, purchasing power parity; billions of international dollars.

This repository is intended for educational and visualization-redesign purposes. It documents a reproducible workflow for extracting and reshaping IMF data and does not claim ownership of the underlying values.

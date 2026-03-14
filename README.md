# largest-economies-information-visualization

A reproducible data-preparation and redesign-planning workflow for a Tableau visualization project based on the IMF World Economic Outlook (WEO) dataset and a HowMuch-derived benchmark dataset. The project focuses on historical GDP (PPP) rankings by country for the benchmark years **1980, 1990, 2000, 2010, 2020, 2021, and 2022**.

The broader goal is to critique and redesign the HowMuch graphic *“Largest Economies in the World Over the Last 40 Years”* using principles from Jonathan Schwabish, Edward Tufte, and Dunford. This repository does **not** claim authorship of the IMF data; it documents a transparent extraction, cleaning, and Tableau-preparation workflow for educational and visualization purposes.

---

## Project overview

This repository now supports a **two-view redesign strategy** rather than a single chart replacement.

The redesigned Tableau work should include:

1. a **clean shared rank chart** (connected-dot / slope-style rank view) for cross-country comparison, and
2. a **rank matrix / highlight table with concise analytical story labels** to surface the most important takeaways.

This change reflects the design tradeoffs discovered during prototyping:
- the original race-style chart preserved comparison but became tangled,
- small multiples improved traceability but weakened shared comparison,
- a plain matrix was too table-like on its own,
- so the best compromise is a **paired redesign**: one view for comparison, one view for interpretation.

---

## Motivation

The original infographic tells an interesting rank-over-time story, but it overloads that story with too many competing visual elements: dense crossing lines, decorative flags and circular badges, strong region coloring, and evenly spaced time columns despite uneven year intervals. These choices make the chart dramatic, but they also make it harder to follow individual countries accurately and harder to distinguish the key analytical stories.

The purpose of this repository is to separate **data preparation** from **visual redesign**. By creating a clean, reproducible Tableau-ready dataset, the redesign work can focus on clarity, comparison, annotation, and visual hierarchy rather than spreadsheet wrangling.

---

## Assignment context

This repository supports a course project that requires:

- selecting an existing visualization,
- identifying at least three major issues in priority order,
- citing course readings to justify the critique and redesign,
- creating a redesigned Tableau draft,
- and documenting the process with screenshots.

The final report is produced outside this repository. This repository serves as the reproducible technical and planning backbone for that work.

---

## Source visualization and data

- **Visualization selected:** *Largest Economies in the World Over the Last 40 Years* (HowMuch)
- **Underlying data used in this repo:** IMF World Economic Outlook (WEO) Excel export plus a HowMuch-derived benchmark dataset
- **Primary Tableau input:** `largest_economies_top10_combined.csv`
- **Indicator represented:** GDP (PPP), benchmark-year top 10 rankings

---

## Data structure used in Tableau

The main Tableau file is a combined CSV with these key fields:

| Column | Description |
|---|---|
| `source_dataset` | Source version shown in the workbook (`HOWMUCH_IMF_DERIVED` or `IMF_WEO`) |
| `country_id` | Country code |
| `country` | Country name |
| `year` | Benchmark year |
| `rank` | Position within source/year (1 = largest) |
| `gdp_ppp_billions_intl_dollars` | GDP (PPP) value in billions of international dollars |

This structure lets one Tableau workbook switch between the two source versions using a single filter.

---

## Redesign direction

The repository no longer treats small multiples as the primary redesign.

### Current redesign strategy

The current strategy is a **paired redesign**:

### View A — Shared rank chart
A cleaned connected-dot / slope-style rank chart that keeps countries on a common frame so viewers can still compare them directly.

Design goals:
- preserve the original chart’s comparative strength,
- remove flags, badges, and heavy decoration,
- reduce color overload,
- and use direct labels selectively.

### View B — Rank matrix with analytical stories
A rank matrix / highlight table that keeps countries and benchmark years in a common grid, then uses concise story labels and annotations to call out the most important shifts.

Design goals:
- remove line tangles,
- make major stories explicit,
- support source-by-source comparison,
- and give the reader a more interpretive second view than the original infographic.

This two-view approach is closer to what a Schwabish-style redesign would do: choose forms that match specific analytical tasks rather than insisting on one chart type for everything.

---

## Analytical story layer

A key addition to the redesign is a concise **story layer** that may differ by source.

Examples of the kinds of stories the rank matrix can support:
- China’s rise to No. 1
- the United States holding first for decades, then slipping to second
- India’s steady climb into the top tier
- Germany and Japan remaining relatively stable near the top
- late-entry countries appearing only in later benchmark years

These should appear as short callouts, annotations, or dashboard captions in Tableau rather than long paragraphs.

---

## Repository structure

```text
largest-economies-information-visualization/
├── data/
│   └── input/
│       ├── WEOOct2025all.xlsx
│       └── Largest Economies in The World Over the Last 40 Years.xlsx
├── build_largest_economies_data.py
├── largest_economies_top10_combined.csv
├── README.md
├── PROCESS.md
├── READING_PRINCIPLES.md
├── SOURCE_METADATA.md
├── REDESIGN_STEPS.md
├── INSTRUCTIONS.md
└── output/                         # optional generated files
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
- outputs one combined file for Tableau use,
- includes both sources in one table via `source_dataset`.

---

## Recommended Tableau workflow

1. Connect Tableau to `largest_economies_top10_combined.csv`
2. Use `source_dataset` as a dropdown switcher
3. Build **View A**: shared rank chart
4. Build **View B**: rank matrix / highlight table
5. Add concise, source-aware analytical callouts
6. Capture screenshots of both views for the final report

---

## Attribution

**Data source:** International Monetary Fund (IMF), *World Economic Outlook (WEO)* database, October 2025 edition, plus a HowMuch-derived benchmark dataset used for comparison.

This repository exists to document sourcing, cleaning, and redesign planning. It does not claim ownership of the original infographic or the IMF data.
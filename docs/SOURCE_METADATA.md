# Source Metadata

This file records source context that is intentionally kept out of the output CSV columns.

## Source summary

### `IMF_WEO`
- Input file: `data/input/WEOOct2025all.xlsx`
- Workbook section used: `Countries`
- Indicator extracted in script: `PPPGDP`
- Edition context: IMF World Economic Outlook, October 2025
- Publication/update metadata in workbook fields (sampled during project):
  - publication timestamp around `2025-10-14`
  - later update timestamp around `2025-11-19`

Interpretation notes:
- The WEO series can be revised across editions as benchmarks and national accounts are updated.
- Even for historical years (e.g., 2021/2022), values may differ from earlier snapshots used in third-party graphics.

### `HOWMUCH_IMF_DERIVED`
- Input file: `data/input/Largest Economies in The World Over the Last 40 Years.xlsx`
- Provenance: assignment-linked spreadsheet aligned with the HowMuch infographic dataset
- Article context observed during project: infographic labeled as an update around February 2021

Interpretation notes:
- This source reflects a point-in-time snapshot used for the infographic narrative.
- The associated article language includes forward-looking wording for some recent years, so this source may include then-current projections/expectations for parts of the displayed period.
- Country aliases are normalized in script (`USA`, `U.K.`, `Russia`, `China`).

## Why this metadata is separate

The output CSV intentionally stays compact for Tableau:
- `source_dataset`
- `country_id`
- `country`
- `year`
- `rank`
- `gdp_ppp_billions_intl_dollars`

Fields such as source file path, publication timestamps, and projection/revision context are documented here instead of being repeated in every data row.

## Output policy

- Default run:
  - `python build_largest_economies_data.py`
  - writes `output/largest_economies_top10_combined.csv`

- Extended run:
  - `python build_largest_economies_data.py --all-outputs`
  - writes additional source-specific CSV/XLSX and IMF long-format outputs

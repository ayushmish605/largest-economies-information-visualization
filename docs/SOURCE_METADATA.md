# Source metadata

This file tracks source details that are intentionally not stored as columns in the output CSV.

## Inputs used by `build_largest_economies_data.py`

### Source dataset: `IMF_WEO`
- Input file: `data/input/WEOOct2025all.xlsx`
- Sheet: `Countries`
- Indicator: `PPPGDP`
- Context: IMF World Economic Outlook, October 2025 edition

### Source dataset: `HOWMUCH_IMF_DERIVED`
- Input file: `data/input/Largest Economies in The World Over the Last 40 Years.xlsx`
- Context: Assignment-linked spreadsheet aligned with HowMuch infographic values
- Notes: Country-name normalization is applied (`USA`, `U.K.`, `Russia`, `China` aliases)

## Output policy
- Default run (`python build_largest_economies_data.py`) writes one file:
  - `output/largest_economies_top10_combined.csv`
- Extended run (`python build_largest_economies_data.py --all-outputs`) writes additional source-specific CSV/XLSX and IMF long-format files.

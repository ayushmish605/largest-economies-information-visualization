# largest-economies-information-visualization

Reproducible data prep for a Tableau redesign of the HowMuch infographic *“Largest Economies in the World Over the Last 40 Years.”* The workflow combines two sources into one benchmark-year top-10 CSV.

## What this repo does
- Reads IMF WEO data and a HowMuch-linked spreadsheet.
- Harmonizes country names/codes.
- Enforces rank correctness from GDP values within each `source_dataset` + `year`.
- Produces one default Tableau-ready file with a source switcher field.

## Current data output
Default run writes:
- `output/largest_economies_top10_combined.csv`

Columns:
- `source_dataset`
- `country_id`
- `country`
- `year`
- `rank`
- `gdp_ppp_billions_intl_dollars`

## Script usage
Install dependencies:

```bash
pip install -r requirements.txt
```

Default output (single CSV):

```bash
python build_largest_economies_data.py
```

Extended outputs (source-specific CSV/XLSX + IMF long files):

```bash
python build_largest_economies_data.py --all-outputs
```

## Repository structure

```text
largest-economies-information-visualization/
├── data/
│   └── input/
│       ├── WEOOct2025all.xlsx
│       └── Largest Economies in The World Over the Last 40 Years.xlsx
├── build_largest_economies_data.py
├── output/
│   └── largest_economies_top10_combined.csv   # generated
├── docs/
│   ├── INSTRUCTIONS.md
│   ├── PROCESS.md
│   ├── READING_PRINCIPLES.md
│   └── SOURCE_METADATA.md
├── original_infographic.jpg
├── requirements.txt
└── README.md
```

Supporting documentation:
- `docs/INSTRUCTIONS.md`
- `docs/PROCESS.md`
- `docs/READING_PRINCIPLES.md`
- `docs/SOURCE_METADATA.md`

## Tableau note
Use `source_dataset` as a dropdown filter to compare `HOWMUCH_IMF_DERIVED` and `IMF_WEO` in one workbook.

## Attribution
Data comes from IMF WEO (October 2025 edition) and a HowMuch-linked benchmark spreadsheet. This repository documents transformation and redesign workflow; it does not claim ownership of source data or the original infographic.
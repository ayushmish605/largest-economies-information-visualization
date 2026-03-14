import argparse
import re
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = REPO_ROOT / "data" / "input" / "Largest Economies in The World Over the Last 40 Years.xlsx"
OUTPUT_DIR = REPO_ROOT / "output"

SOURCE_DATASET = "HOWMUCH_IMF_DERIVED"
SOURCE_VINTAGE = "2021-update"
SOURCE_FILE = "data/input/Largest Economies in The World Over the Last 40 Years.xlsx"
TARGET_INDICATOR = "PPPGDP"
TARGET_INDICATOR_LABEL = (
    "Gross domestic product (GDP), Current prices, Purchasing power parity (PPP) international dollar"
)

COUNTRY_NORMALIZATION = {
    "USA": "United States",
    "U.K.": "United Kingdom",
    "Russia": "Russian Federation",
    "China": "China, People's Republic of",
}

COUNTRY_ID_MAP = {
    "United States": "USA",
    "Japan": "JPN",
    "Germany": "DEU",
    "Italy": "ITA",
    "France": "FRA",
    "Brazil": "BRA",
    "United Kingdom": "GBR",
    "Saudi Arabia": "SAU",
    "Mexico": "MEX",
    "India": "IND",
    "China, People's Republic of": "CHN",
    "Russian Federation": "RUS",
    "Indonesia": "IDN",
}


def parse_rank_cell(value: str):
    text = str(value).strip()
    match = re.match(r"^(.*?)\s*\(\$([0-9.]+)([TB])\)$", text)
    if not match:
        return None

    country_raw, amount_str, unit = match.groups()
    amount = float(amount_str)
    value_billions = amount * 1000 if unit == "T" else amount
    return country_raw.strip(), value_billions


def build_dataframe() -> pd.DataFrame:
    print("Reading HowMuch spreadsheet...")
    raw = pd.read_excel(INPUT_FILE, header=None)

    header_row_index = -1
    for index, row in raw.iterrows():
        values = [str(v).strip().lower() for v in row.values if pd.notna(v)]
        if "year" in values:
            if not isinstance(index, int):
                raise ValueError("Detected header row index is not an integer.")
            header_row_index = index
            break

    if header_row_index < 0:
        raise ValueError("Could not locate the header row containing 'Year'.")

    headers = [str(h).strip() if pd.notna(h) else h for h in raw.iloc[header_row_index].tolist()]
    data = raw.iloc[header_row_index + 1 :].copy()
    data.columns = headers

    records = []
    for _, row in data.iterrows():
        year_value = row.get("Year")
        if pd.isna(year_value):
            continue

        year = int(year_value)

        for rank in range(1, 11):
            cell = row.get(f"Rank {rank}")
            if pd.isna(cell):
                continue

            parsed = parse_rank_cell(cell)
            if parsed is None:
                continue

            country_raw, value_billions = parsed
            country = COUNTRY_NORMALIZATION.get(country_raw, country_raw)

            records.append(
                {
                    "source_dataset": SOURCE_DATASET,
                    "source_vintage": SOURCE_VINTAGE,
                    "source_file": SOURCE_FILE,
                    "country_id": COUNTRY_ID_MAP.get(country, ""),
                    "country": country,
                    "indicator_id": TARGET_INDICATOR,
                    "indicator": TARGET_INDICATOR_LABEL,
                    "scale": "Billions",
                    "unit": "",
                    "year": year,
                    "rank": rank,
                    "gdp_ppp_billions_intl_dollars": value_billions,
                }
            )

    if not records:
        raise ValueError("No rank/value records were parsed from the HowMuch spreadsheet.")

    return pd.DataFrame(records).sort_values(["year", "rank"]).reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert HowMuch top-10 spreadsheet.")
    parser.add_argument(
        "--all-outputs",
        action="store_true",
        help="Write extended XLSX output in addition to default top-10 CSV.",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    unified_df = build_dataframe()
    top10_csv_path = OUTPUT_DIR / "howmuch_infographic_years_top10.csv"
    unified_df.to_csv(top10_csv_path, index=False)

    print(f"Parsed rows: {len(unified_df)}")
    print(f"Saved top-10 CSV to: {top10_csv_path}")

    if not args.all_outputs:
        print("Done. (default mode: top-10 CSV only)")
        return

    legacy_columns = [
        "country_id",
        "country",
        "indicator_id",
        "indicator",
        "scale",
        "unit",
        "year",
        "gdp_ppp_billions_intl_dollars",
    ]
    legacy_df = unified_df[legacy_columns].copy()

    legacy_xlsx_path = OUTPUT_DIR / "howmuch_infographic_years_top10.xlsx"
    legacy_df.to_excel(legacy_xlsx_path, index=False)

    print("Saved extended outputs (legacy XLSX file).")
    print("Done.")


if __name__ == "__main__":
    main()

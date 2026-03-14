import argparse
import re
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = REPO_ROOT / "output"

INPUT_IMF_FILE = REPO_ROOT / "data" / "input" / "WEOOct2025all.xlsx"
INPUT_IMF_SHEET = "Countries"
INPUT_HOWMUCH_FILE = REPO_ROOT / "data" / "input" / "Largest Economies in The World Over the Last 40 Years.xlsx"

TARGET_INDICATOR = "PPPGDP"

START_YEAR = 1980
END_YEAR = 2022
INFOGRAPHIC_YEARS = [1980, 1990, 2000, 2010, 2020, 2021, 2022]

SOURCE_DATASET_IMF = "IMF_WEO"
SOURCE_DATASET_HOWMUCH = "HOWMUCH_IMF_DERIVED"

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

OUTPUT_COLUMNS = [
    "source_dataset",
    "country_id",
    "country",
    "year",
    "rank",
    "gdp_ppp_billions_intl_dollars",
]


def build_imf_long_dataframe() -> pd.DataFrame:
    print("Reading IMF WEO file...")
    df = pd.read_excel(INPUT_IMF_FILE, sheet_name=INPUT_IMF_SHEET)

    required_columns = [
        "COUNTRY.ID",
        "COUNTRY",
        "INDICATOR.ID",
        "INDICATOR",
        "SCALE",
        "UNIT",
        "FREQUENCY",
    ]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing expected IMF columns: {missing}")

    year_columns = [col for col in df.columns if isinstance(col, int)]
    year_columns = [year for year in year_columns if START_YEAR <= year <= END_YEAR]
    if not year_columns:
        raise ValueError("No IMF year columns found in expected range.")

    filtered = df[
        (df["INDICATOR.ID"] == TARGET_INDICATOR)
        & (df["FREQUENCY"].astype(str).str.lower() == "annual")
    ].copy()

    if filtered.empty:
        raise ValueError("No IMF rows found for PPPGDP with annual frequency.")

    keep_columns = ["COUNTRY.ID", "COUNTRY"] + year_columns

    long_df = filtered[keep_columns].melt(
        id_vars=["COUNTRY.ID", "COUNTRY"],
        value_vars=year_columns,
        var_name="year",
        value_name="gdp_ppp_billions_intl_dollars",
    )

    long_df = long_df.rename(
        columns={
            "COUNTRY.ID": "country_id",
            "COUNTRY": "country",
        }
    )

    long_df["year"] = long_df["year"].astype(int)
    long_df["gdp_ppp_billions_intl_dollars"] = pd.to_numeric(
        long_df["gdp_ppp_billions_intl_dollars"],
        errors="coerce",
    )
    long_df = long_df.dropna(subset=["gdp_ppp_billions_intl_dollars"]).copy()

    long_df = long_df.sort_values(["year", "gdp_ppp_billions_intl_dollars"], ascending=[True, False])
    long_df["rank"] = long_df.groupby("year").cumcount() + 1
    long_df["source_dataset"] = SOURCE_DATASET_IMF

    return long_df


def parse_rank_cell(value: str):
    text = str(value).strip()
    match = re.match(r"^(.*?)\s*\(\$([0-9.]+)([TB])\)$", text)
    if not match:
        return None

    country_raw, amount_str, unit = match.groups()
    amount = float(amount_str)
    value_billions = amount * 1000 if unit == "T" else amount
    return country_raw.strip(), value_billions


def build_howmuch_top10_dataframe() -> pd.DataFrame:
    print("Reading HowMuch-linked file...")
    raw = pd.read_excel(INPUT_HOWMUCH_FILE, header=None)

    header_row_index = -1
    for index, row in raw.iterrows():
        values = [str(v).strip().lower() for v in row.values if pd.notna(v)]
        if "year" in values:
            if not isinstance(index, int):
                raise ValueError("Detected HowMuch header row index is not an integer.")
            header_row_index = index
            break

    if header_row_index < 0:
        raise ValueError("Could not locate the 'Year' header row in HowMuch file.")

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
                    "source_dataset": SOURCE_DATASET_HOWMUCH,
                    "country_id": COUNTRY_ID_MAP.get(country, ""),
                    "country": country,
                    "year": year,
                    "rank": rank,
                    "gdp_ppp_billions_intl_dollars": value_billions,
                }
            )

    if not records:
        raise ValueError("No HowMuch top-10 records were parsed.")

    return pd.DataFrame(records).sort_values(["year", "rank"]).reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build largest economies datasets from both sources.")
    parser.add_argument(
        "--all-outputs",
        action="store_true",
        help="Write extended source-specific and XLSX outputs in addition to the default combined CSV.",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    imf_long_df = build_imf_long_dataframe()
    imf_top10_df = (
        imf_long_df[imf_long_df["year"].isin(INFOGRAPHIC_YEARS)]
        .groupby("year", group_keys=False)
        .head(10)
        .copy()
    )
    imf_top10_df = imf_top10_df[OUTPUT_COLUMNS].copy()

    howmuch_top10_df = build_howmuch_top10_dataframe()[OUTPUT_COLUMNS].copy()

    combined_top10_df = (
        pd.concat([imf_top10_df, howmuch_top10_df], ignore_index=True)
        .sort_values(["source_dataset", "year", "rank"])
        .reset_index(drop=True)
    )

    combined_csv_path = OUTPUT_DIR / "largest_economies_top10_combined.csv"
    combined_top10_df.to_csv(combined_csv_path, index=False)
    print(f"Saved combined top-10 CSV to: {combined_csv_path}")

    if not args.all_outputs:
        print("Done. (default mode: one combined CSV)")
        return

    imf_top10_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.csv"
    howmuch_top10_csv_path = OUTPUT_DIR / "howmuch_infographic_years_top10.csv"

    imf_top10_df.to_csv(imf_top10_csv_path, index=False)
    howmuch_top10_df.to_csv(howmuch_top10_csv_path, index=False)

    combined_xlsx_path = OUTPUT_DIR / "largest_economies_top10_combined.xlsx"
    combined_top10_df.to_excel(combined_xlsx_path, index=False)

    imf_long_csv_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.csv"
    imf_long_xlsx_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.xlsx"
    imf_long_df[OUTPUT_COLUMNS].to_csv(imf_long_csv_path, index=False)
    imf_long_df[OUTPUT_COLUMNS].to_excel(imf_long_xlsx_path, index=False)

    imf_infographic_long_df = imf_long_df[imf_long_df["year"].isin(INFOGRAPHIC_YEARS)][OUTPUT_COLUMNS].copy()
    imf_infographic_long_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.csv"
    imf_infographic_long_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.xlsx"
    imf_infographic_long_df.to_csv(imf_infographic_long_csv_path, index=False)
    imf_infographic_long_df.to_excel(imf_infographic_long_xlsx_path, index=False)

    imf_top10_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.xlsx"
    howmuch_top10_xlsx_path = OUTPUT_DIR / "howmuch_infographic_years_top10.xlsx"
    imf_top10_df.to_excel(imf_top10_xlsx_path, index=False)
    howmuch_top10_df.to_excel(howmuch_top10_xlsx_path, index=False)

    print("Saved extended source-specific and XLSX outputs.")
    print("Done.")


if __name__ == "__main__":
    main()

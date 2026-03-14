import argparse
import pandas as pd
from pathlib import Path

# ============================================================
# CONFIG
# ============================================================
REPO_ROOT = Path(__file__).resolve().parents[1]

INPUT_FILE = REPO_ROOT / "data" / "input" / "WEOOct2025all.xlsx"
INPUT_SHEET = "Countries"

# Output folder
OUTPUT_DIR = REPO_ROOT / "output"

# IMF WEO indicator code for:
# GDP, current prices, purchasing power parity; billions of international dollars
TARGET_INDICATOR = "PPPGDP"

SOURCE_DATASET = "IMF_WEO"
SOURCE_VINTAGE = "2025-10"
SOURCE_FILE = "data/input/WEOOct2025all.xlsx"

# Years wanted for the full Tableau dataset
START_YEAR = 1980
END_YEAR = 2022

# Years shown in the infographic
INFOGRAPHIC_YEARS = [1980, 1990, 2000, 2010, 2020, 2021, 2022]


def build_long_dataframe() -> pd.DataFrame:
    print("Reading Excel file...")
    df = pd.read_excel(INPUT_FILE, sheet_name=INPUT_SHEET)

    print(f"Loaded sheet '{INPUT_SHEET}' with shape: {df.shape}")

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
        raise ValueError(f"Missing expected columns: {missing}")

    year_columns = [col for col in df.columns if isinstance(col, int)]
    year_columns = [y for y in year_columns if START_YEAR <= y <= END_YEAR]

    if not year_columns:
        raise ValueError("No year columns from 1980 to 2022 were found.")

    print(f"Found year columns from {min(year_columns)} to {max(year_columns)}")

    filtered = df[
        (df["INDICATOR.ID"] == TARGET_INDICATOR)
        & (df["FREQUENCY"].astype(str).str.lower() == "annual")
    ].copy()

    print(f"Rows after filtering to {TARGET_INDICATOR} and Annual: {filtered.shape[0]}")

    if filtered.empty:
        raise ValueError("No rows found for PPPGDP with annual frequency.")

    keep_columns = [
        "COUNTRY.ID",
        "COUNTRY",
        "INDICATOR.ID",
        "INDICATOR",
        "SCALE",
        "UNIT",
    ] + year_columns

    filtered = filtered[keep_columns].copy()

    long_df = filtered.melt(
        id_vars=["COUNTRY.ID", "COUNTRY", "INDICATOR.ID", "INDICATOR", "SCALE", "UNIT"],
        value_vars=year_columns,
        var_name="year",
        value_name="gdp_ppp_billions_intl_dollars",
    )

    long_df = long_df.rename(
        columns={
            "COUNTRY.ID": "country_id",
            "COUNTRY": "country",
            "INDICATOR.ID": "indicator_id",
            "INDICATOR": "indicator",
            "SCALE": "scale",
            "UNIT": "unit",
        }
    )

    long_df["year"] = long_df["year"].astype(int)
    long_df["gdp_ppp_billions_intl_dollars"] = pd.to_numeric(
        long_df["gdp_ppp_billions_intl_dollars"], errors="coerce"
    )
    long_df = long_df.dropna(subset=["gdp_ppp_billions_intl_dollars"]).copy()

    long_df = long_df.sort_values(["year", "gdp_ppp_billions_intl_dollars"], ascending=[True, False])
    long_df["rank"] = long_df.groupby("year").cumcount() + 1
    long_df["source_dataset"] = SOURCE_DATASET
    long_df["source_vintage"] = SOURCE_VINTAGE
    long_df["source_file"] = SOURCE_FILE

    print(f"Long-format dataset shape: {long_df.shape}")
    return long_df


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract IMF WEO PPPGDP data.")
    parser.add_argument(
        "--all-outputs",
        action="store_true",
        help="Write extended long-format/XLSX outputs in addition to the default top-10 CSV.",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)

    long_df = build_long_dataframe()
    infographic_df = long_df[long_df["year"].isin(INFOGRAPHIC_YEARS)].copy()
    top10_df = infographic_df.groupby("year", group_keys=False).head(10).copy()

    unified_columns = [
        "source_dataset",
        "source_vintage",
        "source_file",
        "country_id",
        "country",
        "indicator_id",
        "indicator",
        "scale",
        "unit",
        "year",
        "rank",
        "gdp_ppp_billions_intl_dollars",
    ]

    top10_unified_df = top10_df[unified_columns].copy()
    top10_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.csv"
    top10_unified_df.to_csv(top10_csv_path, index=False)
    print(f"Saved top-10 CSV to: {top10_csv_path}")

    if not args.all_outputs:
        print("Done. (default mode: top-10 CSV only)")
        return

    full_csv_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.csv"
    full_xlsx_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.xlsx"
    long_df.to_csv(full_csv_path, index=False)
    long_df.to_excel(full_xlsx_path, index=False)

    infographic_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.csv"
    infographic_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.xlsx"
    infographic_df.to_csv(infographic_csv_path, index=False)
    infographic_df.to_excel(infographic_xlsx_path, index=False)

    legacy_top10_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.xlsx"
    top10_df.to_excel(legacy_top10_xlsx_path, index=False)

    print("Saved extended outputs (CSV/XLSX files).")
    print("Done.")


if __name__ == "__main__":
    main()

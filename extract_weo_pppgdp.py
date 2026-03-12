import pandas as pd
from pathlib import Path

# ============================================================
# CONFIG
# ============================================================
INPUT_FILE = "WEOOct2025all.xlsx"
INPUT_SHEET = "Countries"

# Output folder
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# IMF WEO indicator code for:
# GDP, current prices, purchasing power parity; billions of international dollars
TARGET_INDICATOR = "PPPGDP"

# Years wanted for the full Tableau dataset
START_YEAR = 1980
END_YEAR = 2022

# Years shown in the infographic
INFOGRAPHIC_YEARS = [1980, 1990, 2000, 2010, 2020, 2021, 2022]


# ============================================================
# LOAD DATA
# ============================================================
print("Reading Excel file...")
df = pd.read_excel(INPUT_FILE, sheet_name=INPUT_SHEET)

print(f"Loaded sheet '{INPUT_SHEET}' with shape: {df.shape}")

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================
required_columns = [
    "COUNTRY.ID",
    "COUNTRY",
    "INDICATOR.ID",
    "INDICATOR",
    "SCALE",
    "UNIT",
    "FREQUENCY"
]

missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(f"Missing expected columns: {missing}")

# Find numeric year columns that are actually in the sheet
year_columns = [col for col in df.columns if isinstance(col, int)]
year_columns = [y for y in year_columns if START_YEAR <= y <= END_YEAR]

if not year_columns:
    raise ValueError("No year columns from 1980 to 2022 were found.")

print(f"Found year columns from {min(year_columns)} to {max(year_columns)}")

# ============================================================
# FILTER TO THE TARGET SERIES
# ============================================================
filtered = df[
    (df["INDICATOR.ID"] == TARGET_INDICATOR) &
    (df["FREQUENCY"].astype(str).str.lower() == "annual")
].copy()

print(f"Rows after filtering to {TARGET_INDICATOR} and Annual: {filtered.shape[0]}")

if filtered.empty:
    raise ValueError("No rows found for PPPGDP with annual frequency.")

# ============================================================
# KEEP ONLY RELEVANT COLUMNS
# ============================================================
keep_columns = [
    "COUNTRY.ID",
    "COUNTRY",
    "INDICATOR.ID",
    "INDICATOR",
    "SCALE",
    "UNIT"
] + year_columns

filtered = filtered[keep_columns].copy()

# ============================================================
# RESHAPE WIDE -> LONG FOR TABLEAU
# ============================================================
long_df = filtered.melt(
    id_vars=["COUNTRY.ID", "COUNTRY", "INDICATOR.ID", "INDICATOR", "SCALE", "UNIT"],
    value_vars=year_columns,
    var_name="year",
    value_name="gdp_ppp_billions_intl_dollars"
)

# Clean up column names
long_df = long_df.rename(columns={
    "COUNTRY.ID": "country_id",
    "COUNTRY": "country",
    "INDICATOR.ID": "indicator_id",
    "INDICATOR": "indicator",
    "SCALE": "scale",
    "UNIT": "unit"
})

# Ensure clean types
long_df["year"] = long_df["year"].astype(int)
long_df["gdp_ppp_billions_intl_dollars"] = pd.to_numeric(
    long_df["gdp_ppp_billions_intl_dollars"],
    errors="coerce"
)

# Drop rows where GDP is missing
long_df = long_df.dropna(subset=["gdp_ppp_billions_intl_dollars"]).copy()

# Sort by year descending GDP so rank is easy to inspect
long_df = long_df.sort_values(["year", "gdp_ppp_billions_intl_dollars"], ascending=[True, False])

print(f"Long-format dataset shape: {long_df.shape}")

# ============================================================
# SAVE FULL TABLEAU-FRIENDLY DATASET (1980–2022)
# ============================================================
csv_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.csv"
xlsx_path = OUTPUT_DIR / "weo_pppgdp_1980_2022_long.xlsx"

long_df.to_csv(csv_path, index=False)
long_df.to_excel(xlsx_path, index=False)

print(f"Saved full long CSV to:  {csv_path}")
print(f"Saved full long XLSX to: {xlsx_path}")

# ============================================================
# SAVE INFOGRAPHIC YEARS ONLY
# ============================================================
infographic_df = long_df[long_df["year"].isin(INFOGRAPHIC_YEARS)].copy()

infographic_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.csv"
infographic_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_long.xlsx"

infographic_df.to_csv(infographic_csv_path, index=False)
infographic_df.to_excel(infographic_xlsx_path, index=False)

print(f"Saved infographic-years CSV to:  {infographic_csv_path}")
print(f"Saved infographic-years XLSX to: {infographic_xlsx_path}")

# ============================================================
# SAVE TOP 10 PER INFOGRAPHIC YEAR
# ============================================================
top10_df = (
    infographic_df
    .groupby("year", group_keys=False)
    .head(10)
    .copy()
)

top10_csv_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.csv"
top10_xlsx_path = OUTPUT_DIR / "weo_pppgdp_infographic_years_top10.xlsx"

top10_df.to_csv(top10_csv_path, index=False)
top10_df.to_excel(top10_xlsx_path, index=False)

print(f"Saved top-10 CSV to:  {top10_csv_path}")
print(f"Saved top-10 XLSX to: {top10_xlsx_path}")

print("Done.")

# Process log

This file documents the steps completed so far for the redesign project based on the "Largest Economies in the World Over the Last 40 Years" visualization.

## Step-by-step process

1. Read the original article and study the infographic titled "The World's Biggest Economies Over Time" (update: February 2021; published September 23, 2025).
   - The original infographic image is saved in this repo as `original_infographic.jpg` for reference during critique and redesign.
   
   ![Original infographic showing the world's biggest economies over time](original_infographic.jpg)
2. Identified the source of the data as the International Monetary Fund (IMF) World Economic Outlook (WEO) database, Table 1.1, and confirmed the indicator used in the infographic is GDP at current prices, purchasing power parity (PPPGDP), measured in billions of international dollars.
3. Obtained the IMF WEO Excel export and saved it in the repository as `WEOOct2025all.xlsx`.
4. Wrote a beginner-friendly Pandas script (`extract_weo_pppgdp.py`) to:
   - load the WEO Excel sheet,
   - filter to the `PPPGDP` indicator and annual frequency,
   - keep years 1980 through 2022,
   - reshape the data into a tidy, long format with one row per country-year,
   - and export Tableau-ready CSV/XLSX outputs.
5. Generated three output datasets in the `output/` folder:
   - full long-format dataset for 1980 to 2022,
   - a subset for the infographic benchmark years (1980, 1990, 2000, 2010, 2020, 2021, 2022),
   - and a top-10-per-year subset for those benchmark years.
6. Updated the repository documentation to explain the purpose of the project, the data source, and how the cleaned files are intended for Tableau redesign work.

## Current status

- Data source identified and saved in the repo.
- Extraction and reshaping script completed.
- Tableau-ready outputs generated locally (not committed).
- README updated to reflect the assignment context.

## Next steps (outside this repository)

1. Build the redesigned visualization in Tableau using the long-format dataset.
2. Take screenshots of the redesign and insert them near the written critique.
3. Write the required critique (three issues, 300 to 350 words each) with APA in-text citations and a Works Cited section.
4. Submit the final Word document for the assignment.

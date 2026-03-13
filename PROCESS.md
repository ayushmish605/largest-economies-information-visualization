# Process log

This file documents the steps completed so far for the redesign project based on the "Largest Economies in the World Over the Last 40 Years" visualization.

## Step-by-step process

1. Read the original article and study the infographic titled "The World's Biggest Economies Over Time" (update: February 2021; published September 23, 2025).
   - The original infographic image is saved in this repo as `original_infographic.jpg` for reference during critique and redesign.
   
   ![Original infographic showing the world's biggest economies over time](original_infographic.jpg)

   **Detailed description and visual analysis**
   The infographic presents the top 10 GDP (PPP) rankings across seven benchmark years (1980, 1990, 2000, 2010, 2020, 2021, 2022). The layout is a grid of columns by year, with ranks 1 through 10 listed vertically on the left. Each country is shown as a circular badge containing the country name and GDP value, and a colored ring indicates region (North America, Europe, Asia, Latin America). The countries are connected year-to-year with thick, curved lines that trace rank changes over time, producing a slope-like effect across the columns.

   **Color and grouping**
   Color encodes region through the ring around each circle: red for North America, green for Europe, yellow for Asia, and orange for Latin America. These hues are saturated and high-contrast, which makes regional grouping pre-attentive, but the strong color also competes with the rank and value labels inside the circles. The connecting lines use the same hue as the region, reinforcing grouping but adding additional visual density where lines overlap.

   **Pre-attentive features (per Schwabish)**
   - **Position on a common scale:** Rank is encoded by vertical position, which is a high-accuracy channel. The consistent row positions allow quick detection of rank changes.
   - **Color hue:** Region is encoded by hue and is immediately visible, but it is not the primary analytic question, so it can distract from rank changes.
   - **Connectedness and line direction:** The connecting lines create a strong sense of continuity and motion across time, which helps follow a country’s path but also produces line crossings that reduce clarity.
   - **Enclosure/shape:** The country values are enclosed in circles, which makes them stand out as discrete items but increases ink and reduces space for labels.
   - **Text density:** Each circle includes both country name and GDP value, which increases cognitive load and makes it harder to scan quickly.

   **Other notable features**
   - The chart shows many rank swaps across the benchmark years, producing a dense tangle of overlapping lines; the intersections themselves do not encode additional meaning and function as chartjunk rather than data.
   - The line crossings create a "clusterf***" effect in Dunford's terms, making it difficult to follow a single country across all years without losing the trail.
   - Flags help distinguish countries, but they introduce strong color contrasts that compete with the GDP value text. The U.S. flag, in particular, creates a vibrating effect against the numeric labels, reducing legibility.
   - The region legend (colored circle borders) adds a categorical variable, which aligns with Tufte's idea of "escaping flatland" by encoding more dimensions, but it also forces repeated legend lookups and slows comprehension.
   - The year spacing is inconsistent (decades from 1980–2020, then one-year steps for 2021 and 2022). Because the horizontal spacing is uniform, viewers may overestimate the magnitude of changes in the last two columns relative to earlier decades.
2. Identified the source of the data as the International Monetary Fund (IMF) World Economic Outlook (WEO) Excel export and confirmed the indicator used in the infographic is GDP at current prices, purchasing power parity (`PPPGDP`), measured in billions of international dollars.
   - Instead of relying on the secondary spreadsheet linked in the assignment, I located the primary IMF WEO source to preserve data accuracy and authenticity.
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
7. Refined the redesign strategy after evaluating chart alternatives:
   - Initially considered a bump-chart-centered redesign because it preserves rank-over-time movement.
   - After testing the implications of line density and label crowding, shifted to a small-multiples redesign as the primary direction.
   - Retained a simplified bump chart as an exploratory backup for comparison.

## Current status

- Data source identified from the IMF World Economic Outlook (WEO) Excel export and saved in the repo.
- Extraction and reshaping script completed.
- Tableau-ready outputs generated locally (not committed).
- Redesign direction refined: small multiples selected as primary Tableau draft; simplified bump chart retained as exploratory backup.
- Documentation updated to reflect assignment context and redesign iteration.

## Next steps (outside this repository)

1. Build the small-multiples Tableau redesign using the long-format dataset.
2. Optionally test a simplified bump chart for side-by-side comparison.
3. Take screenshots of both the process and the improved final draft for the assignment document.
4. Write the required critique (three issues, 300 to 350 words each) and tie each issue to the redesign decision using APA in-text citations and a Works Cited section.
5. Submit the final Word document for the assignment.

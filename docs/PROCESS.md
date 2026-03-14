# Process Log: Data Sourcing, Verification, and Tableau Preparation

This document explains the actual step-by-step process used to identify the source data behind the HowMuch infographic, verify the relevant IMF series, extract the needed values, and prepare a unified CSV file for use in Tableau.

The goal of this process was not only to recreate the chart data, but also to make the workflow transparent and reproducible. Because the final Tableau redesign compares a HowMuch-derived dataset with a directly sourced IMF WEO dataset, the process had to document where each value came from and how the two source streams were combined.

---

## 1. Starting point: the assigned infographic

The project began with the chart assigned in the course materials: HowMuch’s **“Largest Economies in the World Over the Last 40 Years.”**

That infographic shows the top-ranked economies at a small set of benchmark years:

- 1980
- 1990
- 2000
- 2010
- 2020
- 2021
- 2022

The infographic labels the measure as **GDP (PPP)** and includes a source note pointing to the **International Monetary Fund**. However, the chart itself is not a raw IMF table; it is a visual derivative created by HowMuch. That meant the first task was to determine exactly which IMF series the infographic was using.

---

## 2. Identifying the likely IMF source

The next step was to inspect the wording of the infographic carefully.

Two clues were especially important:

1. the chart title refers to **GDP (PPP)**
2. the footnote states that the values are shown in **current prices in international dollars**

Those clues strongly suggested that the underlying data series came from the IMF **World Economic Outlook (WEO)** database and, more specifically, from the series commonly labeled **PPPGDP**.

That indicator corresponds to GDP at:

- current prices
- purchasing power parity (PPP)
- measured in **billions of international dollars**

This matched the structure of the HowMuch chart much more closely than nominal GDP in domestic currency or GDP growth rates.

---

## 3. Confirming that the IMF WEO dataset contained the needed years

After identifying the likely IMF series, the next task was to verify that the IMF data actually covered the years shown in the infographic.

At first, there was uncertainty because some IMF web interfaces seemed to show only a shorter time window. To resolve that, the full IMF WEO spreadsheet export was obtained and examined directly.

The relevant workbook was:

- `WEOOct2025all.xlsx`

The workbook was checked programmatically to confirm:

- that the historical year columns extended back to **1980**
- that the **PPPGDP** indicator existed in the data
- that the file contained annual country-level entries for the benchmark years used in the infographic

This was an important validation step, because it showed that the historical data did exist in the IMF export even if some web views made it less obvious.

---

## 4. Inspecting the WEO workbook structure

Once the workbook was available, the next step was to understand its structure.

The useful sheet for country-level analysis was the **`Countries`** sheet. Each row represented a country-indicator combination, and the year values appeared in wide format across many columns.

The relevant identifying columns included items such as:

- country code
- country name
- indicator code
- indicator description
- frequency
- unit

The year columns then extended across the sheet, including the benchmark years required for the project.

The workbook had to be filtered to isolate the PPP GDP series only.

---

## 5. Programmatically extracting the IMF WEO PPPGDP series

To avoid manual filtering and copying inside Excel, a Pandas script was written to extract the IMF values into a Tableau-friendly format.

The extraction process did the following:

1. loaded the WEO Excel workbook
2. selected the `Countries` sheet
3. filtered the rows to the **`PPPGDP`** indicator
4. kept only annual values
5. retained the benchmark years needed for the infographic
6. reshaped the wide year columns into a long format suitable for Tableau

This produced a clean IMF-based dataset containing:

- source information
- country name
- country code
- year
- GDP value

At this stage, the IMF data source had been isolated independently from the infographic itself.

---

## 6. Reconstructing the HowMuch-derived dataset

The next challenge was that the HowMuch infographic is not a downloadable raw dataset in the same structure as the IMF workbook.

Because of that, the values used in the infographic had to be reconstructed from the chart itself and its displayed benchmark-year values.

This derived dataset was built specifically to represent the HowMuch chart as published, rather than to replace or override the IMF data.

The purpose of doing this was analytical transparency:

- one source stream reflects the **published infographic values**
- the other source stream reflects the **direct IMF WEO values**

That distinction matters because the infographic is a secondary visual product, while the WEO export is the primary data source.

---

## 7. Matching countries and benchmark years across both datasets

Once both source streams existed, the next task was to standardize them so they could be compared inside Tableau.

This required using the same benchmark years for both:

- 1980
- 1990
- 2000
- 2010
- 2020
- 2021
- 2022

It also required normalizing country identifiers so that countries lined up consistently across the two sources.

The final unified structure needed to use the same columns regardless of whether a row came from the HowMuch-derived values or the IMF WEO values.

---

## 8. Writing Pandas scripts to create a unified long-format CSV

After extracting and standardizing both source streams, a Pandas workflow was written to produce a single combined CSV file.

This was one of the most important steps in the project, because Tableau works best when the data is tidy and consistent.

The scripts were designed to:

1. take the IMF-extracted values
2. take the HowMuch-derived values
3. normalize their schema
4. append them together into one long-format table
5. add a source identifier so each row could always be traced back to its origin

The final combined file included fields such as:

- `source_dataset`
- `country_id`
- `country`
- `year`
- `rank`
- `gdp_ppp_billions_intl_dollars`

This made it possible to build a single Tableau workbook that could switch between source versions using a filter or parameter rather than requiring separate workbooks.

---

## 9. Explicitly labeling the source of each row

A crucial part of the workflow was the addition of the `source_dataset` field.

This field was included so the combined Tableau dataset would remain transparent. Instead of blending the values into one ambiguous table, each row was tagged as belonging to one of two categories:

- `HOWMUCH_IMF_DERIVED`
- `IMF_WEO`

This design choice made the dashboard and worksheets much more informative, because the viewer can explicitly switch between:

- the values represented in the published infographic
- the directly sourced IMF WEO values

That source labeling is one of the most important transparency features in the final project.

---

## 10. Checking and correcting ranking consistency

After the combined CSV was built, the rank field was checked against the GDP values to make sure the ordering was internally consistent within each source-year group.

This check was necessary because the HowMuch-derived dataset had been reconstructed from a published infographic rather than pulled directly from a structured table.

Programmatic checks revealed a few ranking inconsistencies in the HowMuch-derived rows, including examples where two countries were out of order relative to the GDP values stored in the CSV.

Those inconsistencies were then corrected so that, within each source-year group:

- higher GDP implied a better rank
- ties could be reviewed explicitly
- the Tableau views would not present contradictory position/value relationships

This correction step improved the integrity of the derived dataset without erasing the fact that it came from a secondary visual source.

---

## 11. Preparing the final Tableau input file

The final Tableau input file was designed to support an easy and flexible user experience.

Instead of requiring separate uploads for separate sheets, the project uses one unified CSV that can power multiple views. This made the Tableau work much easier because:

- the same file could feed both final charts
- the same source switcher could be reused across views
- sorting and story logic could be controlled in one workbook

This final CSV was intentionally created in a **long format**, because Tableau handles long-format data more cleanly for filtering, legends, dynamic sorting, and multiple view types.

---

## 12. Why the GitHub repository matters

The GitHub repository is not just a storage location for the final charts. It is part of the documentation of the process.

The repository includes:

- the raw and processed data files
- the Pandas scripts used to transform the source data
- the process notes
- the redesign rationale
- the Tableau preparation logic

This matters because part of the project’s integrity comes from showing exactly how the data was sourced and transformed.

In particular, the repository helps clarify:

- how the IMF WEO data was identified
- how the HowMuch-derived values were represented
- how the two source streams were combined
- how the final CSV was built for Tableau

---

## 13. Resulting workflow summary

In chronological order, the full process was:

1. start from the assigned HowMuch infographic
2. inspect its title and footnotes to infer the likely IMF source
3. identify **PPPGDP** in the IMF WEO dataset as the relevant series
4. obtain the full IMF WEO Excel export
5. confirm that the benchmark years back to 1980 were present
6. inspect the workbook structure and isolate the `Countries` sheet
7. write Pandas code to extract the PPP GDP values from IMF WEO
8. reconstruct the benchmark-year values represented in the HowMuch infographic
9. standardize both datasets into a matching schema
10. write Pandas scripts to combine them into a single long-format CSV
11. add a `source_dataset` field so every row remained traceable
12. verify that the ranks matched the GDP values and correct inconsistencies
13. use the unified CSV as the main Tableau input file

---

## 14. Why this process was necessary

This process was more extensive than simply downloading a chart dataset because the assignment involved both critique and redesign. To redesign responsibly, it was important to understand not only what the infographic showed, but also where the values came from and how they were transformed.

The final Tableau workbook therefore rests on a sourcing and processing workflow that is:

- documented
- reproducible
- transparent
- and explicit about the difference between the direct IMF data and the HowMuch-derived values

That workflow is central to the credibility of the final redesign.
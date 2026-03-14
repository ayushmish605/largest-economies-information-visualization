# Redesign Steps

## Part A — Core diagnosis

The original infographic still has three main problems:

1. **Tangled trajectories**
   - too many crossings make individual country paths hard to follow

2. **Decorative overload**
   - flags, circular badges, and strong region coloring compete with the ranking task

3. **Unequal time intervals shown with equal spacing**
   - 1980–2020 are decade steps, while 2020–2022 are one-year steps

A successful redesign should preserve the interesting comparison story while reducing these decoding costs.

---

## Part B — New redesign decision

The project should no longer pursue a single-chart solution as the only answer.

### New primary direction: paired redesign

The new final Tableau work should include two coordinated views:

### View A — Shared rank chart
A cleaned connected-dot / slope-style chart that keeps all countries on a common frame for cross-country comparison.

### View B — Rank matrix / highlight table with concise story labels
A companion matrix that removes the tangle and explicitly surfaces the key takeaways through short annotations.

### Why this is the stronger compromise

- A full original-style bump chart keeps comparison but becomes too tangled.
- Small multiples improve traceability but weaken shared comparison.
- A plain rank matrix is too table-like by itself.
- Pairing a shared comparison view with an interpretive matrix solves more of the original problems at once.

This is the redesign direction the project should now follow.

---

## Part C — Tableau setup common to both views

### Step 1 — Connect the combined CSV
Use:

`largest_economies_top10_combined.csv`

### Step 2 — Validate field roles
Recommended field roles:
- `source_dataset` → Dimension
- `country` → Dimension
- `country_id` → Dimension
- `year` → Dimension
- `rank` → Measure / numeric
- `gdp_ppp_billions_intl_dollars` → Measure / numeric

### Step 3 — Add the source switcher
1. Drag `source_dataset` to **Filters**.
2. Keep both values selected.
3. Show the filter.
4. Change it to **Single Value (dropdown)**.

The workbook should be able to switch between:
- `HOWMUCH_IMF_DERIVED`
- `IMF_WEO`

### Step 4 — Keep source-specific screenshots
Because the story labels may differ slightly by source, plan to take screenshots for both dropdown settings.

---

## Part D — View A: shared rank chart

## Goal
Preserve cross-country comparison while removing most of the original graphic’s clutter.

## Build steps

1. Start a new worksheet.
2. Put `year` on **Columns**.
3. Put `rank` on **Rows**.
4. Reverse the rank axis so rank 1 is at the top.
5. Set Marks to **Line** or **Line + Circle** if Tableau makes that easy.
6. Put `country` on **Detail**.
7. Keep the line color restrained:
   - either all light gray with selective highlighting later,
   - or very muted category colors.
8. Add `gdp_ppp_billions_intl_dollars` to **Tooltip**.
9. Add labels sparingly:
   - only at the line ends if possible,
   - or only for a small number of focus countries.

## Design rules for View A
- no flags
- no circular badges
- no bright region outlines
- thin lines
- direct labels only where readable
- subtitle noting unequal time intervals

## What this view is for
This is the comparison view. It should answer:
- who is above whom,
- who rose,
- who fell,
- and when major position changes happened.

---

## Part E — View B: rank matrix / highlight table with story labels

## Goal
Create a second view that removes line tangles entirely and makes the main stories explicit.

## Important note
This should **not** be just a plain table of numbers. It should function as a visual analytic companion.

## Structure
- rows = countries
- columns = benchmark years
- cell text = rank
- tooltip = GDP value and source
- optional subtle color = rank band or emphasis

## Build steps

1. Start a new worksheet.
2. Put `country` on **Rows**.
3. Put `year` on **Columns**.
4. Put `rank` on **Text**.
5. Put `gdp_ppp_billions_intl_dollars` on **Tooltip**.
6. Keep marks as **Text** or convert to a **highlight table** if Tableau formatting supports it cleanly.
7. Sort countries in a meaningful order, preferably by 2022 rank or another defensible reference order.
8. Use very restrained color, if any:
   - for example, a light sequential background or subtle emphasis for the top ranks.

## Story layer
Add concise analytical annotations near or alongside the matrix. These should be short and readable, not paragraph-length.

### Candidate story types
- **China reaches No. 1**
- **United States falls from a long-held top rank to No. 2**
- **India steadily climbs into the top tier**
- **Germany and Japan remain relatively stable near the top**
- **Some countries appear only in later benchmark years**

## Important source note
These stories should be checked separately under:
- `HOWMUCH_IMF_DERIVED`
- `IMF_WEO`

Some wording may need to change slightly depending on the source shown.

## How to add stories in Tableau
Possible beginner-friendly methods:
- dashboard text boxes next to the matrix
- worksheet title/subtitle notes
- annotations on selected cells
- small caption text under the chart

The best option is whichever stays concise and clean.

---

## Part F — Recommended final dashboard structure

If Tableau layout time permits, the best final presentation is a simple dashboard with:

### Left or top
**View A — Shared rank chart**

### Right or bottom
**View B — Rank matrix with concise story labels**

### Shared control
`source_dataset` dropdown

This lets the reader:
- compare countries directly,
- then read the clarified story view,
- and switch the whole dashboard between the two source versions.

---

## Part G — Screenshot plan

Keep the screenshot set simple.

### Recommended screenshots
1. **Shared rank chart draft**
2. **Rank matrix / highlight table draft**
3. **Final paired redesign dashboard or strongest combined arrangement**
4. Optional: one source-switched comparison screenshot if useful in the report

---

## Part H — What to say in the write-up

The write-up should explain that the redesign evolved after testing alternatives.

Suggested summary:
- The original chart preserved comparison but was too tangled.
- Small multiples reduced clutter but weakened cross-country comparison.
- A plain matrix alone was too table-like.
- The final redesign therefore used two coordinated views: a shared rank chart for comparison and a rank matrix with concise story labels for interpretation.

That is the strongest concise explanation of the current design decision.
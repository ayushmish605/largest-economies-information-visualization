# Process Log

## Project goal

Build a reproducible workflow for critiquing and redesigning the HowMuch infographic *“Largest Economies in the World Over the Last 40 Years”* using benchmark GDP (PPP) rankings from IMF-based data, then prepare Tableau views that better align with course principles on clarity, perceptual accuracy, and purposeful design.

---

## Data sourcing and preparation

### Initial source question
The first task was confirming whether IMF WEO actually contained the historical GDP (PPP) data needed for the benchmark years shown in the infographic.

### Source confirmation
The IMF WEO export does contain the relevant series for historical PPP GDP. The project then shifted from source discovery to source extraction and transformation.

### Combined Tableau dataset
A combined CSV was created so one Tableau workbook could switch between:
- `HOWMUCH_IMF_DERIVED`
- `IMF_WEO`

This avoided maintaining two separate Tableau workbooks and made source comparison more transparent.

---

## Redesign evolution

### Phase 1 — Original intuition: cleaned bump chart
The initial redesign idea was a simplified bump chart because the source visualization is fundamentally a rank-over-time graphic. This preserved the comparative structure but still risked line tangles.

### Phase 2 — Small multiples pivot
The next redesign direction was small multiples. This improved traceability and eliminated crossings, but it also weakened cross-country comparison because countries no longer shared one clear comparison frame.

### Phase 3 — Matrix / highlight-table idea
A rank matrix was then considered because it removes line tangles and keeps rows and columns aligned. On its own, though, a plain matrix risked becoming too table-like and under-visual.

### Current direction — Paired redesign
The current redesign direction is a **paired solution**:

1. **Shared rank chart** for direct comparison across countries
2. **Rank matrix / highlight table with concise analytical story labels** for interpretation

This is the strongest compromise found so far. It keeps the comparative insight of a shared chart while also giving the reader a clearer, more analytical second view.

---

## Why the paired redesign is stronger

The original graphic’s biggest problems are still:
1. tangled trajectories and cluttered crossings,
2. decorative flags and badges that compete with the data,
3. misleading equal spacing of unequal time intervals.

The paired redesign addresses these better than any single prototype tested so far:

- **Shared rank chart** preserves comparison while stripping away decoration.
- **Rank matrix** removes tangles entirely and highlights specific patterns.
- **Story labels** add interpretation rather than forcing the viewer to infer every key takeaway alone.

---

## Story-layer insight

A major new insight in the redesign process is that the final visualization should not rely only on structure and marks. It should also include a concise story layer.

Examples of likely stories:
- China rises from lower ranks to No. 1 by the later benchmark years.
- The United States remains dominant for decades, then moves to No. 2.
- India steadily climbs into the upper ranks.
- Some countries are stable near the top; others appear only later.

Because the workbook can switch between `HOWMUCH_IMF_DERIVED` and `IMF_WEO`, these annotations may need to be checked and lightly adjusted by source.

---

## Current status

Completed:
- data source confirmed,
- combined Tableau CSV prepared,
- source switcher built into the planned workflow,
- multiple redesign directions tested conceptually and in Tableau,
- primary redesign strategy revised from “small multiples only” to a paired redesign.

Current preferred final direction:
- View A: shared rank chart
- View B: rank matrix / highlight table with concise analytical stories

---

## Next steps

1. Build the final shared rank chart in Tableau.
2. Build the companion rank matrix / highlight table.
3. Add concise story labels or annotations.
4. Test both source versions with the `source_dataset` dropdown.
5. Capture screenshots for the final report.
6. Tie the redesign decision back to the readings in the write-up.
# Directions
Use the material available from one of the following sources for your re-drawn visualization project:

## Source options
- **Largest Economies in The World Over the Last 40 Years**
  - **Visualization:** https://howmuch.net/articles/worlds-biggest-economies-over-time
  - **Spreadsheet:** Largest Economies in The World Over the Last 40 Years.xlsx
- **Fastest growing occupations in the U.S.**
  - **Visualization:** https://howmuch.net/articles/fastest-growing-occupations-in-the-US
  - **Spreadsheet:** Charting the 20 Top Growing U.S. Careers Based on Real Salary Projections.xlsx
- **Putting Apple's Value into Perspective**
  - **Visualization:** https://howmuch.net/articles/putting-apple-into-perspective
  - **Spreadsheet:** Apples Value Into Perspective.xlsx

## Big idea
The goal of this assignment is to brainstorm how an existing visualization could be remade and then execute a redesigned draft in Tableau. The written critique and the technical draft should both apply ideas from the course readings, especially Schwabish’s chapter on redesigning visualizations, along with other course concepts from Schwabish, Tufte, and the Dunford article.

## Required deliverables
- Create a Word document with your name at the top and identify which chart you selected, including a screenshot of the original chart.
- Identify **at least three major issues** with the chart **in priority order** and write a brief description of each with concrete suggestions for improvement; 300-350 words per issue is a good target, for roughly 900-1050 words total.
- Cite course readings to explain why each aspect of the visualization needs to be fixed and how you propose to fix it, using APA in-text citations and a Works Cited section.
- Execute a redesigned version of the graph in Tableau using the data from the selected source. Take a screenshot (or multiple screenshots) of your work, making sure the improvements are visible, and place it near the discussion of the fixes.
- Save and submit the final Word document.

## Point breakdown
- Writing quality/issues; clarity and quality of argument for the critique and redesign (70)
- Quality of Tableau redesign (70)
- Participation in March 11 discussion (10)
- **Total: 150 points**

## Notes for this repository
- **Selected chart:** Largest Economies in The World Over the Last 40 Years (HowMuch)
- **Data source used in this repo:** IMF World Economic Outlook (WEO) Excel export, indicator `PPPGDP` (GDP at current prices, purchasing power parity; billions of international dollars)
- **Process and critique notes:** See [PROCESS.md](PROCESS.md)
- **Visualization principles and course-reading references:** See [READING_PRINCIPLES.md](READING_PRINCIPLES.md)
- **Tableau redesign plan and implementation workflow:** See [REDESIGN_STEPS.md](REDESIGN_STEPS.md)
- **Project reminder:** The assignment explicitly allows multiple screenshots and even breaking the redesign into smaller graphs, which supports a small-multiples-first workflow
- **Current script behavior:** The unified script `build_largest_economies_data.py` generates one combined top-10 CSV by default in `output/`; use `--all-outputs` when you need extended source-specific or long/XLSX artifacts

## Selected visualization

- **Original chart:** *Largest Economies in the World Over the Last 40 Years* (HowMuch)
- **Underlying data used in this repo:** IMF World Economic Outlook (WEO) benchmark data plus a HowMuch-derived benchmark dataset
- **Primary Tableau file:** `largest_economies_top10_combined.csv`

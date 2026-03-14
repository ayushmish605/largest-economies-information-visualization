# Principles from course readings

This document consolidates key visualization principles from the assigned readings so they can be cited directly later without re-opening the PDFs. Quotes are verbatim and include APA-style in-text citations with page numbers (or paragraph/page markers where available).

These principles are used to justify both the critique of the original infographic and the redesign decision process. The redesign may compare alternatives (for example, bump chart versus small multiples) rather than assume one universally correct chart type.

For data-source implementation details (file names, source context, and output policy), see `docs/SOURCE_METADATA.md`.

---

## Schwabish - Better Data Visualizations (Ch. 1-2: Visual Processing and Perceptual Rankings)

1. **Choose encodings based on how accurately readers can perceive values.**
   Quote: "When we consider how to visualize our data, we must ask ourselves how accurately the reader can perceive the data values" (Schwabish, 2021, p. 1).

2. **Encodings on a common baseline are easiest to compare.**
   Quote: "It is easier to compare the data in line charts, bar charts, and area charts that have the same axis or baseline" (Schwabish, 2021, p. 1).

3. **Unaligned axes reduce accuracy.**
   Quote: "Graphs on which the data are positioned on unaligned axes ... are slightly harder for us to accurately discern the values" (Schwabish, 2021, p. 1).

4. **Angle, area, volume, and color are lower-precision encodings.**
   Quote: "Farther down the vertical axis are encodings based on angle, area, volume, and color" (Schwabish, 2021, p. 1).

5. **Common charts are common because they are accurate and familiar.**
   Quote: "Standard graphs, like bar and line charts, are so common because they are perceptually more accurate, familiar to people, and easy to create" (Schwabish, 2021, p. 15).

6. **Nonstandard charts can increase engagement even if precision drops.**
   Quote: "Spurring readers to engage with a graph is sometimes just as important" (Schwabish, 2021, p. 15).

7. **Visualization balances analytical precision and engagement.**
   Quote: "Data visualization is a mix of science and art" (Schwabish, 2021, p. 17).

8. **Engagement can justify tradeoffs in perceptual accuracy.**
   Quote: "Sometimes you must make your visuals interesting and engaging, even at the cost of absolute perceptual accuracy" (Schwabish, 2021, p. 17).

9. **If a chart is unfamiliar, explain how to read it.**
   Quote: "To overcome these hurdles, you may need to explain how to read the graph" (Schwabish, 2021, p. 18).

---

## Schwabish - Better Data Visualizations (Ch. 13: Redesigns)

1. **Redesign is about clarity, not shaming the original author.**
   Quote: "My goal is not to criticize these chart creators or their efforts but to demonstrate how the lessons we have learned can be applied to making data visualizations cleaner, clearer, and more effective" (Schwabish, 2021, p. 13).

2. **There is no single correct redesign.**
   Quote: "There is no 'right' or 'wrong' approach, just different ways of making improvements" (Schwabish, 2021, p. 13).

3. **Match chart type to analytical task.**
   Quote: "If the goal with this chart is to show relative trends in acreage among five crops, a bar chart is a poor choice" (Schwabish, 2021, p. 370).

4. **Line charts can reveal relative trends more clearly than grouped bars.**
   Quote: "We could redesign this as a simple line chart. Here, the drop in acreage for cotton is very clear" (Schwabish, 2021, p. 370).

5. **Direct labeling can replace a legend and improve readability.**
   Quote: "I didn't use a legend here ... but instead added the labels at the end of each line" (Schwabish, 2021, p. 370).

6. **Small multiples can increase space but reduce comparability.**
   Quote: "The advantage is that there's more space for the graph ... The disadvantage is that relative patterns are slightly less clear" (Schwabish, 2021, p. 372).

7. **Stacked bars hide comparisons when baselines differ.**
   Quote: "We can clearly discern the differences between the values of the blue series ... We are not as well equipped, however, to similarly assess the values for the other series, because they don't share the same baseline" (Schwabish, 2021, p. 372).

8. **Use equal scales across panels in small multiples.**
   Quote: "The important point with making a graph like this is that the horizontal space for each series is the same" (Schwabish, 2021, p. 373).

---

## Tufte - Envisioning Information (Ch. 1: Escaping Flatland)

1. **The core task is representing multivariate reality on a flat surface.**
   Quote: "Escaping this flatland is the essential task of envisioning information" (Tufte, 1990, p. 1).

2. **Increase dimensionality and information density where possible.**
   Quote: "[These methods] work to increase (1) the number of dimensions that can be represented on plane surfaces and (2) the data density (amount of information per unit area)" (Tufte, 1990, p. 1).

3. **Communication is constrained by the 2D surface.**
   Quote: "All communication between the readers of an image and the makers of an image must now take place on a two-dimensional surface" (Tufte, 1990, p. 1).

4. **Every escape from flatland involves tradeoffs.**
   Quote: "Nearly every escape from flatland demands extensive compromise, trading off one virtue against another" (Tufte, 1990, p. 15).

---

## Tufte - Beautiful Evidence (Ch. 5: Principles of Analytical Design)

1. **Excellent graphics embody analytical principles.**
   Quote: "Excellent graphics exemplify the deep fundamental principles of analytical design in action" (Tufte, 2006, p. 123).

2. **Strong graphics document method, scales, and sources.**
   Quote: "A title announces the design method ... A paragraph of text explains the color code, the 3 scales of measurement, and the methods. Five data sources are acknowledged" (Tufte, 2006, p. 123).

---

## Dunford - When data visualization really isn't useful (and when it is)

1. **Visualization is about communicating data to a wider audience.**
   Quote: "The chief benefit of data visualization is the ability to communicate data to a wider audience" (Dunford, n.d., p. 1).

2. **Too many pie slices reduce clarity.**
   Quote: "There is such a thing as too many segments in a pie chart. Instead of hundreds, try 3. And certainly no more than 6" (Dunford, n.d., p. 2).

3. **Avoid counterintuitive color scales in heat maps.**
   Quote: "We're wired to see the darkest or strongest color as having the highest amount of something" (Dunford, n.d., p. 4).

4. **Do not use 3D unless it encodes data.**
   Quote: "If you see a 3D chart that's 3D for no reason ... then you should question the data, the chart, the maker, and everything based on the chart" (Dunford, n.d., p. 7).

5. **Do not truncate axes in bar charts.**
   Quote: "As bar charts use length as their visual cue, truncating the axis will over-dramatize the differences" (Dunford, n.d., p. 8).

6. **Avoid cherry-picking timeframes to exaggerate change.**
   Quote: "Yau also points out how easy it is to cherry-pick dates and timeframes to fit a particular narrative" (Dunford, n.d., p. 10).

7. **Dual axes can imply false correlation.**
   Quote: "They're sometimes used to imply correlation or even causation" (Dunford, n.d., p. 11).

8. **Use distinct, consistent colors and clear keys.**
   Quote: "The colors are distinctly different and consistent throughout the chart and you've got the key on the side so there's no confusion as to what the individual colors mean" (Dunford, n.d., p. 20).

9. **Common mistakes include wrong chart type, too many variables, poor scaling, and bad color choices.**
   Quote: "Wrong type of chart" and "Too many variables" appear alongside "Improper scaling" and "Poor color choices" as common mistakes (Dunford, n.d., p. 21).

---

## Works cited

Dunford. (n.d.). When data visualization really isn't useful (and when it is). Tempo.io. https://www.tempo.io/blog/good-and-bad-data-visualization

Schwabish, J. (2021). Better data visualizations: A guide for scholars, researchers, and wonks. Columbia University Press.

Tufte, E. R. (1990). Envisioning information. Graphics Press.

Tufte, E. R. (2006). Beautiful evidence. Graphics Press.

---

## How these principles now inform the redesign

The current redesign strategy is:

### View A — Shared rank chart
This addresses the need for direct comparison. It keeps countries in one frame, but removes the original’s decorative overload.

### View B — Rank matrix / highlight table with story labels
This addresses the need for clearer interpretation. It removes tangled paths and supports concise analytical callouts.

### Why both views are justified
A single chart has struggled to balance:
- cross-country comparison,
- traceability over time,
- and interpretive clarity.

Using two coordinated views is therefore a principled redesign choice, not an admission of failure. It reflects the idea that one form may not be optimal for every analytical task.

---

## Redesign takeaway

The final redesign should not be judged only by whether it “looks cleaner.” It should be judged by whether it better supports:
- direct comparison,
- accurate reading,
- and clear interpretation.

That is why the project now pursues a paired redesign with a shared comparison view and an annotated matrix view.
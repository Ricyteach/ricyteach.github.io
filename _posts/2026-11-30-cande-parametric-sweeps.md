---
layout: article
title: "One Buried Structure Run Tells You Almost Nothing"
description: "A single soil-structure interaction analysis answers one question about one set of assumptions, and the assumptions are the least certain part of the problem. What a sweep across cover height, wall thickness, and soil stiffness reveals that a single run conceals."
related:
  - "what-is-cande"
  - "running-legacy-software"
service_page: "/cande-buried-structures/"
---

When I explained [what CANDE is](/articles/what-is-cande/), I made the point that the program is only as good as the soil assumptions going into it. I want to follow that further, because it has a consequence that changes how the analysis should be run.

A buried structure analysis has two categories of input. The first category is well known: the pipe or culvert geometry, the material properties, the wall thickness or gage, the live load model. The second category is estimated: the stiffness of the backfill, the degree of compaction that will actually be achieved, the properties of the native soil beside the trench, the friction at the interface between the structure and the soil. The second category frequently controls the answer, and it is the category nobody can measure in advance.

A single run takes one set of values from each category and produces one result. It is a precise answer to a question containing several guesses.

## What a sweep shows

The alternative is to run the model across ranges rather than at points, which produces something a single run cannot: the shape of the response.

Sweeping cover height shows where the governing condition changes. Shallow cover under live load and deep cover under dead load are different problems, and many structures have a range in between where neither is severe. A design checked only at the maximum specified cover can miss the shallow condition entirely, and the reverse is equally common.

Sweeping wall thickness or gage shows how much margin the selected section actually has. Two designs can both pass, with one sitting comfortably in a flat region of the response and the other perched on a slope where a small change in an assumption moves it across the limit. The passing report looks identical for both. The sweep does not.

Sweeping soil stiffness is the one that matters most and gets done least. Run the same structure with the backfill modulus varied across the plausible range for the specified material and compaction, and you learn how much of your result depends on the contractor achieving the compaction in the specification. If the answer barely moves, you have a robust design and you can say so. If the answer moves a great deal, you have a design that depends on field quality control, and the right response is to say that in the report rather than to hope.

## Sensitivity is the deliverable

That last point is the real argument. A buried structure design produces numbers, but what the owner actually needs to know is which assumption the design depends on.

A structure whose thrust and deflection are insensitive to backfill modulus across the range of realistic values is a structure that will behave acceptably whether or not installation goes perfectly. A structure whose deflection doubles between the low and high ends of the same range is telling you that the installation specification is a structural requirement rather than a preference, and it deserves an explicit note in the drawings and a different level of inspection during construction.

You cannot distinguish those two cases from a single run. Both produce a passing report with a number that satisfies the criterion.

## Why this required automation

Running a model across three ranges means a few dozen to a few hundred analyses, which is impractical by hand, so the reason I can work this way is the [automation of the program itself](/articles/running-legacy-software/).

The obstacles were the ones that article describes, plus one specific to this program. The design criteria results, the checks that state whether thrust, buckling, plastic penetration, and seam strength are satisfied, do not appear in the structured output file. They exist only in the printed text report. A batch process that collects results from the structured output alone will assemble a complete looking table with the engineering conclusions missing from it, which is the sort of thing you discover only if you go looking.

So the automation reads the text report, and the values it extracts are checked against the program's own display for at least one run in every batch before I read any of the rest.

## What I do with the output

The result of a sweep is a set of tables and a short written interpretation: here is the governing cover condition, here is the margin at the selected section, here is how much the answer depends on backfill quality, and here is the range of installation conditions under which the design remains adequate.

That is a more useful document than a single analysis, and it is frequently cheaper than the sequence of separate analyses that gets commissioned when the cover height changes, then the gage changes, then someone asks what happens if the compaction comes in low. Doing all of it at once costs a batch running overnight.

It also makes the review easier. A reviewer reading a single analysis has to decide whether they believe the soil assumptions. A reviewer reading a sweep can see what happens if the assumptions are wrong, which is a question they can answer for themselves.

If you have a buried structure, a culvert rehabilitation, or a relining project where the installation conditions are uncertain, the range is the useful answer. That work is the core of my [buried structure practice](/cande-buried-structures/).

---
layout: article
title: "Drawings Written in Python"
description: "Producing dimensioned, scaled drawings from code rather than from a drafting session. What it suits, what it does not, and the parts that are harder than people expect."
related:
  - "calculator-as-deliverable"
  - "ai-checking-work"
service_page: "/structural-engineering/"
---

A drawing and a calculation describe the same structure. On most projects they are produced by different means, at different times, and the drawing gets updated when the calculation changes, which is a process that works exactly as well as the discipline of the person doing it.

There is a category of drawing where that separation is unnecessary. If the geometry of a detail follows directly from the calculation that sized it, the drawing can be generated from the same data, and then the two cannot disagree. That is the case for producing drawings from code.

## What this suits

Repeated details are the obvious case. A foundation detail that appears in twenty variants across a product line, a connection detail parameterized by member size, a base plate layout that follows from the anchor design: all of these are the same drawing with different numbers, and drafting each one by hand is both slow and an invitation to inconsistency between them.

Drawings that follow from a calculation are the second case. When the shaft depth, the reinforcement, and the concrete section come out of an analysis, the detail showing them is a rendering of the result. Producing it from the analysis output means a change to the analysis propagates to the drawing automatically, rather than through a note to myself to update the detail.

Drawing sets that need to be produced many times are the third. A company selling an engineered product needs a stamped drawing for each order. Generating the set from the order parameters is the only approach that stays economical past the first dozen.

## What it does not suit

Anything requiring layout judgment. Deciding how to break a building into sheets, what to show in a section and what to leave out, how to arrange details so a reviewer can follow them: that is drafting as a discipline, and it does not reduce to parameters.

Anything drawn once. The effort to parameterize a detail is real, and for a single detail on a single project it exceeds the effort of drawing it. I use a drafting session for one-off work and I expect to keep doing so.

Anything where the geometry is genuinely irregular. Existing conditions, field-measured structures, and renovations rarely have the kind of regularity that makes generation worthwhile.

## The parts that are harder than they look

People assume the difficulty is in computing the geometry. The geometry is the easy part. The difficulty is in everything that makes a drawing readable.

Layers and line weights have to follow a consistent standard, because a drawing where everything is the same weight is technically complete and visually unusable. The hierarchy that makes a drawing readable at a glance, heavy lines for cut material, medium for visible edges, light for hidden and for dimensions, is a convention that has to be encoded deliberately.

Text height interacts with scale in a way that catches everyone once. Text is specified at its height on the printed sheet, and the model is drawn at full size, so the text height in model space depends on the scale of the viewport it will be seen through. Get it wrong and the annotation is either microscopic or enormous, and the error is invisible until the sheet is plotted.

Dimension styles have the same problem, multiplied. Arrow size, extension line offset, text gap, and the overall scale factor all have to be set consistently with the plot scale, and a dimension style that looks correct in one viewport is wrong in the next one at a different scale.

Paper space and viewports are where drawings from code most often go wrong, because the geometry lives at full size in model space and the sheet shows a scaled window onto it. Setting up the sheet, the title block, the viewport, and the scale correctly is the part that determines whether a plot is usable, and it is entirely separate from the part that draws the structure.

Tables and multileaders have their own difficulties, including the specific and frustrating case of a table that has all its data and none of its grid lines, because the style controls the visibility of the lines independently of the content.

None of that is intellectually demanding. All of it has to be right, and the only way to know it is right is to plot the sheet and look at it.

## Verification is the whole problem

This is the reason I have been slower to call this work finished than the analysis tooling, and I have said as much when writing about the [toolkit](/articles/ai-toolkit/) before.

A generated calculation that is wrong usually announces itself. The numbers are implausible, the units are off, something fails to converge. A generated drawing that is wrong looks like a drawing. Every line is crisp, every dimension has a value, the title block is populated, and the detail shows a connection that cannot be built. There is no internal signal.

So the checking has to be external, and it has to be systematic. The dimensions on the drawing get compared against the values in the calculation that produced them, which is a task well suited to the kind of [consistency checking](/articles/ai-checking-work/) I wrote about earlier, since it is literal cross-referencing between two documents. The geometry gets checked for constructability by a person, because no automated check knows that a bolt cannot be installed where a weld already is. And the sheet gets plotted and read as a plan reviewer would read it, because a drawing that is correct and illegible is not finished.

## What it is actually for

The benefit is narrower than it sounds and more valuable than it sounds. A drawing produced from the same data as the calculation cannot contradict the calculation. That specific class of error, where the detail shows a reinforcement pattern that the calculation superseded two revisions ago, stops being possible.

That is one error class removed, permanently, from the deliverables where this applies. It pairs naturally with the [parametric calculator work](/articles/calculator-as-deliverable/), where the calculation and the drawing are both outputs of the same engineering done once.

If you have a repeated detail, an engineered product line, or a drawing that keeps falling out of step with the calculation behind it, that is the situation this addresses, under my [structural engineering services](/structural-engineering/).

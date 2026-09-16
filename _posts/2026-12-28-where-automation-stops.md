---
layout: article
title: "Where I Stop Automating"
description: "The closing article of the series, and the counterweight to the tooling articles. The specific decisions that stay with the engineer, and why the half of the work that got faster is not the half you are hiring."
related:
  - "ai-toolkit"
  - "calculation-package"
service_page: "/sap2000-ai-automation/"
---

This series has spent a lot of words on tools. Generating model input, driving programs that cannot be scripted, sweeping analyses across ranges, producing drawings from code, reading calculation sheets nobody wants to change. It would be reasonable to finish the year with an article about what comes next.

Instead I want to be specific about the boundary, because the tooling is only defensible if the boundary is real, and a boundary that is asserted rather than described is not worth much.

## Deciding what the structure is

Nothing I have built participates in this and nothing I expect to build will.

Before there is a model there is a decision about what is being modeled. A contractor sends photographs, a partial set of drawings from 1974, and a description of what they want to do. Somewhere between those inputs and an analysis there is a judgment about what the structure actually is: which elements are participating, which are along for the ride, where the load goes, what is holding it up now and whether that mechanism will still exist after the work.

That judgment determines everything downstream, it is frequently made with incomplete information, and it is not a calculation. Two competent engineers can look at the same building and identify different load paths, and the conversation that resolves it is engineering in its purest form.

## Choosing the soil model

Geotechnical work has a version of this that is sharper, because the choice is explicit and the consequences are large.

A finite element analysis of soil requires a constitutive model and its parameters. A simple model is appropriate for some problems and badly misleading for others. An advanced model represents stiffness behavior more faithfully and requires parameters that the geotechnical report may not contain. Choosing between them, and justifying the parameters against whatever data actually exists, is the analysis. The software that solves the resulting system is doing arithmetic.

Nothing about that choice is automatable, because it depends on what the soil data supports, what the design is sensitive to, and how much conservatism the situation warrants. Those are three judgments, and the last one is partly about consequences rather than about soil.

## Deciding whether a result is believable

This is the boundary that matters most in daily practice, and it is the one people underestimate.

Every program I use will produce a result. It will produce a result when the input is sound and when it is not. It will produce a beautifully rendered deflected shape for a model with a support in the wrong place, a plausible thrust for a buried structure with a backfill modulus off by a factor, and a clean set of member ratios for a frame that was never loaded in the governing direction.

There is no internal signal. The only detection mechanism is an engineer looking at the answer and asking whether the physics is right: is that deflection possible, does the reaction total match the applied load, is the moment diagram the shape it should be for that loading, did the failure occur where failure should occur. That check is fast, it is unglamorous, and it is the single most important thing I do.

Automation makes it more important rather than less. When a batch produces eighty results overnight, nobody reads eighty results carefully. So the habit has to become structural: check the physics on a sample from every batch, verify extracted numbers against what the program displays, and treat any batch where the sample disagrees as entirely untrustworthy rather than mostly fine. I described that discipline throughout this series because it is the thing that makes the rest of it usable.

## Accepting responsibility for the seal

Then there is the part that is not a technical boundary at all.

When I seal a drawing or a calculation package, I am stating that I am professionally responsible for it. That responsibility does not divide. There is no portion of it that belongs to a tool, no reduction for the parts that were generated, and no defense available to me that begins with an explanation of how the software works. If it is wrong, it is my error, in front of a licensing board and anyone else who asks.

That is the correct arrangement, and it is the reason the tools are built the way they are. Every one of them is designed so that a human can check its output, because I have to be able to check its output. A tool whose results I could not independently verify would be useless to me regardless of how good it was, because I could not sign for it.

## What you are actually hiring

The tooling has made the mechanical half of engineering considerably faster. The model assembly, the file formats, the repeated runs, the report formatting, the cross-referencing: all of it takes a fraction of the time it used to, and that is a real benefit that shows up in schedules and in fees.

It has not touched the other half. Deciding what the structure is, choosing how to represent the soil, recognizing that an answer is wrong, knowing which limit state actually governs, and standing behind the result: none of that is faster than it was, and none of it is going to be.

A client hiring this practice is hiring the second half. The first half is the reason I can take on the [smaller bounded work](/articles/small-projects/) that larger firms decline, and the reason a parametric study is affordable rather than prohibitive. But the deliverable is judgment, documented well enough that somebody else can [check it](/articles/calculation-package/), with a seal on it.

That was the argument at the start of this series, when I wrote about the [first tool I built](/articles/ai-toolkit/), and after two dozen articles about tooling it is still the argument. The tools are worth having. They are not what you are paying for.

That distinction is the basis of how I work, across [analysis automation](/sap2000-ai-automation/) and everything else in the practice.

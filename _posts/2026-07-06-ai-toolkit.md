---
layout: article
title: "Beyond SAP2000: Building an AI Toolkit Across the Whole Deliverable"
description: "An honest account of where the automation toolkit stands: what is working, what is in development, and how each piece fits into the deliverable pipeline."
---

The SAP2000 model builder was the first tool I built this way, but it was never meant to be the only one. The same approach works anywhere the job is structured data and repetitive assembly carried out under engineering judgment, and that describes a surprising amount of what fills an engineer's week. So I have been building a family of skills across the rest of the deliverable pipeline. Here is where that stands, honestly, including the parts that are not finished.

## Drafting (in development)

A real drawing is not a sketch. It is to scale, dimensioned, annotated, and readable by a fabricator or a plan reviewer who was not in the room when it was designed. I am building tooling that produces genuine DXF drawings from a description: scaled details, sections, framing plans, and the structural notation that goes with them, including weld and bolt symbols, member tags, schedules, general structural notes, and multi-sheet sets.

I will be straight about its status: this one is harder than the SAP2000 work, and it is still in development. A model can be subtly wrong and still produce a drawing that looks fine, which makes the verification problem genuinely difficult. It is producing real drawings today, but I am not going to call it finished, because a drawing that is almost right is worse than useless. It earns the same treatment as everything else here, which is that nothing leaves without an engineer checking it.

## Report writing (working)

A calculation isn't a deliverable until it is documented. The writeup, the assumptions, the code references, the limitations language, all of it has to keep pace with the analysis, and historically it is the part that lags, because it is tedious and it is the last thing standing between you and sending the package. I built a skill that assembles formatted engineering reports with consistent structure and language, so the documentation moves at the speed of the work instead of holding it up. This one is in regular use.

## Load combinations (in development)

Load combinations are exactly the kind of bookkeeping that is mind-numbing by hand and easy to get wrong: the full set of strength and service combinations across the governing code, applied correctly and tracked through the analysis. I am building a skill to generate and check them across the codes I work in. It is not finished yet, and I would rather tell you that than oversell it. It is coming.

## The thread running through all of it

Every one of these is taught the same painstaking way the SAP2000 tool was, and every one of them keeps a licensed engineer in the loop. The tools handle production. They do not handle judgment, and they never get the last word. What they buy back is time: the assembly, the drafting, the documentation, and the bookkeeping that were never really engineering get compressed, so more of the project goes to the part that actually is.

That is the whole strategy. Not a gimmick, and not a promise that a machine will do your engineering. A deliberate, verified automation layer under the parts of the work that deserve to be automated, built and checked by someone who has to sign for the result.

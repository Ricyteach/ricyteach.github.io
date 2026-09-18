---
layout: article
title: "What a Shop Drawing Review Actually Checks"
description: "A fabricator sends a submittal and asks a licensed engineer to review it. What that engagement covers, what it does not transfer, and the five findings that come up over and over."
related:
  - "ai-checking-work"
  - "cold-formed-steel"
service_page: "/shop-drawing-review/"
---

A fabricator builds something well, a general contractor or an owner asks for engineering confirmation, and a set of shop drawings arrives in my inbox. This is one of the most common engagements I take, and it is also the one whose scope gets misunderstood most often, in both directions.

Some people believe a review makes the reviewing engineer responsible for the assembly. Others believe it is a formality that produces a signature. Both readings cause trouble later, so it is worth setting out what the engagement actually covers.

## What the engagement is

A shop drawing review confirms that what the fabricator intends to build satisfies the governing code and agrees with the design intent for the project.

That sentence has two halves and both matter. The code half is objective: the assembly either has the capacity for the loads that apply to it or it does not. The design intent half depends on documents outside the submittal, meaning the project drawings, the specification, and whatever the engineer of record assumed when the assembly was called out.

What the review does not do is transfer responsibility for the fabricator's means, methods, sequences, or field dimensions. It also does not make the reviewer the engineer of record for the structure the assembly attaches to. Those boundaries are standard across the industry, and I write them into the review response every time rather than leaving them understood.

## The order I check in

**Loads first, always.** A wrong load makes every number downstream wrong, and reviewing member capacities against an incorrect demand is a careful waste of an afternoon. So the first question is what wind, snow, seismic, and live loads were applied, what site conditions and exposure they were derived from, and which code edition the authority having jurisdiction has adopted.

This is where the largest errors live. An open structure analyzed with enclosed building pressure coefficients gets loads that are wrong by a substantial margin. A submittal prepared to a code edition the jurisdiction has not adopted is a rejection waiting to happen.

**Then the members and connections.** Capacity against demand for each element shown, with the connections examined at least as closely as the members. In my experience the members are usually adequate and the connections are where the problems are.

**Then the load path out of the assembly.** Every assembly delivers reactions into something else: a slab, a roof structure, a wall, a foundation. A submittal that stops at the base plate has answered half the question. If those reactions exceed what the receiving structure can take, the assembly fails even though every line in the submittal is correct.

**Then internal consistency.** Do the sections agree with the plans, do the schedules agree with the details, do the dimensions close. This is literal cross-referencing across a hundred pages, and it is exactly the work I described in the article on [using artificial intelligence to check an engineer's work](/articles/ai-checking-work/). A machine reading for contradictions does not get tired on page sixty. Every discrepancy it reports is a question for me to evaluate, and most turn out to be nothing.

## The five findings that keep recurring

**Member sizes that differ from the design.** A substitution was made for availability or cost, sometimes for good reason, and the submittal shows the substitute without any demonstration that it is equivalent.

**Connections detailed differently than the design assumed.** The analysis assumed a moment connection and the detail shows a shear tab, or the reverse. This changes the distribution of forces through the whole assembly, and it is invisible unless somebody compares the detail against the assumption behind the calculation.

**Missing bracing.** The member is adequate for its unbraced length as analyzed, and the bracing that produced that unbraced length does not appear anywhere in the submittal.

**Welds that cannot be made in the position shown.** The detail is correct on paper and the welder cannot physically reach the joint once the assembly is erected in the sequence intended. This one is found by looking at the drawing as a fabricator would rather than as an analyst would.

**Dimensions that do not close.** The plan and the section disagree, or a string of dimensions does not sum to the overall. Usually harmless and occasionally the visible edge of a real geometry error.

Thin material has its own version of all five. Manufacturer capacity tables for [cold-formed sections](/articles/cold-formed-steel/) are correct for the conditions they were developed for, which are frequently not the span, loading, or end conditions on your project, so those tables get checked rather than accepted.

## What the response obligates

I sort findings into two categories and the distinction is the practical part of the deliverable.

**Items requiring resolution** are conditions where I cannot conclude the assembly is adequate. Work should not proceed on those elements until they are addressed. Each one cites the drawing, the provision it relates to, and what would resolve it.

**Comments** are observations that do not affect adequacy. A dimension that should be clarified, a note that contradicts another note harmlessly, a detail that would be easier to build a different way. These are offered and the fabricator can take or leave them.

When the required items are resolved, a stamped letter of review follows. When they are not resolvable within the current design, the honest answer is that the submittal needs redesign, which is a separate engagement rather than something I fold into a review.

If you have a submittal that needs engineering review, the scope, the deliverable, and what to send me are set out on my [shop drawing review page](/shop-drawing-review/).

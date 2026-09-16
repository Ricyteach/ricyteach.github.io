---
layout: article
title: "What a Calculation Package Is For"
description: "A calculation package exists so that another engineer, a plan reviewer, or the author three years later can follow the reasoning and confirm it. Why a stack of correct output tables still fails review."
related:
  - "ai-checking-work"
  - "small-projects"
service_page: "/structural-engineering/"
---

A calculation package is an argument, addressed to a reader, that the structure is adequate. Treating it instead as a record that the work was done sounds like a harmless difference in emphasis, until a package comes back from a plan reviewer with comments that all amount to the same complaint, which is that the reviewer cannot tell what was assumed.

I have written packages, reviewed other people's, and had my own returned with comments. The packages that survive review have a specific shape, and it has less to do with the quality of the engineering than people expect.

## Who is actually reading it

Three readers, with different questions.

The plan reviewer wants to confirm that the design satisfies the adopted code, and has limited time and no access to the model. They are looking for the loads, the governing checks, and the code references, and they need to find each one without reading everything.

Another engineer, reviewing for an owner or a lender, wants to know whether the analysis represents the real structure and whether the assumptions are defensible. They will look at the model figures before the numbers.

The third reader is the author, three years later, when something on the project changes and someone asks whether the original design can accommodate it. That reader has forgotten everything and has only the package.

Any of those three can reject a package that contains entirely correct engineering, because correctness that cannot be followed is not usable.

## What belongs in it

**The load derivation, shown.** Not the final loads, the derivation: the code and edition, the site parameters, the intermediate values, and how each load was arrived at. This is the section reviewers read first and the section most often reduced to a summary table. A number that appears without a derivation is a number the reviewer has to take on faith, and reviewers are not obligated to.

**The assumptions, written out as prose.** What was assumed about support conditions, about the condition of existing material, about what the contractor will achieve in the field, about what loads will and will not be present. These are ordinary sentences in plain language, listed together rather than scattered through the calculation. If the design depends on something the reader would not guess, it belongs here.

**Model figures showing what was analyzed.** Not what was intended. A screen capture of the actual model, with the supports, the members, and the applied loads visible, is worth more to a reviewer than pages of numeric output, because it is the only way to confirm that the analysis represents the structure on the drawings. Most of the serious errors I have found in other people's packages were visible in a model figure and invisible in the results.

**The governing checks, identified as governing.** A package containing every check performed, with no indication of which one controls, asks the reader to sort it themselves. Stating which limit state governs, at which location, with what margin, is the conclusion of the argument.

**References to specific provisions.** Give section numbers. A statement that the design was checked per the applicable standard tells a reviewer nothing they can verify.

**The limitations.** What the package does not cover, what remains the responsibility of others, and the conditions under which the conclusions cease to apply. This is the section that protects everyone, and it is the one most often omitted from packages produced under schedule pressure.

## Why output tables alone fail

A package assembled from software output is a record of what the software computed. It contains no statement of what question was asked, and it presents every result at equal weight, so the reader has to reconstruct the engineering from the residue of it.

That reconstruction is work, and it is work the reader did not agree to do. When a reviewer has to reverse engineer the intent from the output, one of two things happens. Either they return the package with comments asking for what should have been there, which costs a cycle, or they approve it without genuinely checking it, which is worse for everyone including the engineer who signed it.

The narrative is what converts a set of results into an argument. It does not have to be long. On a small job it can be two pages in front of the calculations, and on the [small bounded work](/articles/small-projects/) I take on regularly it often is exactly that. What it has to do is state the question, the assumptions, the method, the answer, and the limits.

## The consistency problem

A package assembled over several weeks, through revisions, develops internal contradictions. The load that changed in week two appears at its old value in an appendix. The member size that was increased is correct in the analysis and wrong in the summary. The code edition cited in one section differs from the one used in another.

None of these are engineering errors and all of them will be found by a competent reviewer, at the cost of a review cycle and some credibility. Checking a hundred page document against itself is exactly the [literal cross-referencing](/articles/ai-checking-work/) that people perform badly and machines perform well, and it is the single highest value check to run before a package goes out.

## The test I apply

Before a package leaves, I ask whether a competent engineer who has never seen the project could read it and arrive independently at the same conclusion, without asking me anything.

If the answer is no, the package is incomplete regardless of how correct the analysis is. The engineering is only half the deliverable. The other half is making it possible for someone else to confirm the engineering, and that half is what the package is for.

Preparing packages that survive review, and reviewing other people's, are both part of my [structural engineering services](/structural-engineering/).

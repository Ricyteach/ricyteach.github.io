---
layout: article
title: "What I Look For When I Review Somebody Else's Design"
description: "The reviewer's order of operations, written for people who are about to receive a review. Why the loads get checked first, why most review comments are questions, and what a reviewer does with something that is unclear rather than wrong."
related:
  - "calculation-package"
  - "ai-checking-work"
service_page: "/structural-engineering/"
---

Receiving an engineering review is uncomfortable. Somebody you have never met is going through work you are responsible for, and the comments arrive as a list without much context about how they were arrived at. This article is the other side of that, written for people who are about to be reviewed: here is the order I work in and what each step is actually looking for.

## The loads come first, always

I check the load derivation before I look at anything else, and if the loads are wrong I usually stop there.

The reason is arithmetic. Every number downstream of a load is a function of that load. If the wind pressure is derived for the wrong exposure category, or the snow load omits drifting, or the seismic parameters came from the wrong site class, then every member check in the package is precisely computed and wrong by the same proportion. Reviewing the member checks first means carefully verifying a long series of correct calculations performed on an incorrect premise.

This is also where the most consequential errors actually are. Member design errors tend to be local and modest. Load errors are global and can be large. The open structure that was assigned enclosed building pressure coefficients, the roof designed for balanced snow with no drift case, the foundation designed with strength level loads against an allowable bearing pressure: these are the findings that change a design rather than adjust it.

## Then whether the model is the structure

The second question is whether the analysis represents the thing on the drawings.

I look at the model figures. Where are the supports and are they the restraints the connection details actually provide? A base plate with four anchors drawn as a fixed support may or may not be fixed, and the difference changes the moment distribution through the frame. Are the members continuous where the drawings show them spliced? Does the model include the elements that will be there, and exclude the ones that will not?

This is also where I look for the structure that was analyzed in a convenient configuration rather than the built one. A frame analyzed as a complete assembly that is erected in stages, a member analyzed with lateral support that arrives later in the sequence, a foundation analyzed with backfill on both sides when construction will have it on one: all of these produce results that are correct for a structure that never exists.

If the package has no model figures, this step cannot be performed, which is the practical reason I [insist on them](/articles/calculation-package/) in packages I produce.

## Then the governing limit states

Only at this point do I look at the checks, and I am looking for absence more than error.

Arithmetic errors in a member check are rare in software output and easy to find when they occur. Missing limit states are common and hard to see, because nothing in the package indicates that a check was not performed. A cold-formed member checked for local buckling and not for distortional buckling produces a complete report. An anchorage checked for steel strength and not for concrete breakout produces a passing result. A beam checked for strength and not for deflection satisfies the code and fails in service.

So the question at this stage is which limit states apply to this member in this material under this loading, and which of them appear in the package. The ones that do not appear are the findings.

## Then whether the documents agree

The last technical step is comparing the drawings to the calculations. The reinforcement shown, the member sizes called out, the connection details, the dimensions: these come from the calculations and they drift apart during revisions.

This is literal, tedious cross-referencing, and it is the part of a review where I use the [consistency checking tools](/articles/ai-checking-work/) I have written about, because a machine reading a hundred pages for contradictions does not get tired on page sixty. Every discrepancy it reports is a question for me to evaluate rather than a finding, and most of them turn out to be nothing. The ones that are not nothing are worth the whole exercise.

## What happens with something unclear

A good deal of what a reviewer encounters is neither correct nor incorrect. It is unclear. The package does not say what was assumed, and the result is consistent with two different assumptions, one of which would be fine and one of which would not.

The correct response to that is a question, and this is why most review comments are phrased as questions rather than as findings. A comment asking what was assumed about the support condition at grid line four is not a polite way of saying the support condition is wrong. It usually means exactly what it says: I cannot determine what was assumed, and I need to know before I can agree with the result.

The worst thing a reviewer can do with an ambiguity is resolve it themselves, in the favorable direction, and approve. The second worst is to write it up as an error. Asking is the only response that is both honest and useful.

## How to receive one

Two suggestions, offered from having been on both sides.

Answer the question that was asked. A comment asking how a load was derived wants the derivation. The reviewer already knows you believe the load is correct, and the comment is asking to be shown.

Treat a comment you disagree with as a signal that something was unclear. If a competent reviewer read the package and reached the wrong conclusion about what you did, the package let them. Sometimes the right response is to explain why the approach is correct, and to add the sentence to the package that would have prevented the question.

I perform independent reviews and peer reviews as a regular part of my [structural engineering services](/structural-engineering/), on projects of any size.

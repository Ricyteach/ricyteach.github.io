---
layout: article
title: "A Hundred Anchor Configurations Instead of One"
description: "Anchor design is a small calculation repeated endlessly with different inputs, which makes it worth automating. What an embedment sweep or an edge distance study changes about the conversation."
related:
  - "concrete-anchorage-failure-modes"
  - "calculator-as-deliverable"
service_page: "/sap2000-ai-automation/"
---

The [previous article](/articles/concrete-anchorage-failure-modes/) described the failure modes that govern anchorage to concrete, and made the point that edge distance, spacing, and crack state usually decide the answer rather than the size of the anchor. That has a practical consequence. If the governing variables are geometric, then what a client actually needs is rarely a single answer. They need to know which geometries work.

Anchorage is a small calculation with many inputs, repeated over and over with the numbers changed. That is close to a definition of work worth automating.

## What a single run tells you

A conventional anchor check produces one demand to capacity ratio for one configuration, along with the mode that governs. It answers the question asked. If the answer is that the design fails, it does not tell you what would succeed, and the next step is to change something and run it again, which people do two or three times before settling on whatever passes first.

Running it two or three times gives you a design that works. Running it eighty times gives you the shape of the problem: which variable the answer is actually sensitive to, how much margin the passing configuration has, and how close the next configuration is to the boundary.

## What a sweep looks like

The useful sweeps are the ones over the variables a contractor can actually change on site.

An embedment sweep keeps the anchor pattern fixed and varies the depth, which shows where the governing mode shifts from concrete breakout to steel. That transition point is worth knowing, because a design that governs on steel behaves more predictably under overload than one that governs on breakout.

An edge distance study varies the position of the pattern relative to the free edges. The result is usually a map with a fairly sharp boundary: a region where the anchorage works comfortably, a narrow band where it is marginal, and a region where no reasonable anchor solves it. Handing a contractor that map is far more useful than handing them a single dimension they have to hit exactly.

A diameter comparison across a family of anchors, at a fixed geometry, frequently demonstrates the point from the previous article in the most convincing way available: the demand to capacity ratio barely moves, because the concrete is governing and the concrete does not care how thick the bolt is.

## What it changes about the conversation

The conversation with a contractor or a fabricator stops being a series of binary questions and becomes a single exchange. Instead of "will this work," which produces a yes or a no and then another question three days later when the condition in the field turns out to be different, the answer is a range: any anchor in this family at this embedment works anywhere at least this far from an edge, and here is what happens if you cannot achieve that.

That is a better deliverable for everyone. It survives the discovery that the actual edge distance is smaller than the drawing said, it does not require a new engagement every time a dimension changes, and it puts the boundary of the acceptable region in the contractor's hands rather than in my inbox.

It is the same idea as the [parametric calculator](/articles/calculator-as-deliverable/), applied at a smaller scale and without building a product around it. The engineering is done once, thoroughly, across a defined range, instead of once per phone call.

## The failure mode of the automation itself

There is a specific hazard in automating this kind of check, and it is worth naming because it produces wrong answers quietly.

In the anchor design software I use, the design code and the unit system are stored separately from the calculation inputs. They live in a different part of the file from the geometry and the loads. That separation is invisible when you are working in the interface, because the interface keeps them consistent. It becomes very visible when a program generates input files, because it is entirely possible to write a file whose loads are in one unit system and whose envelope declares another, or whose geometry was set up under one design code while the file claims a different one.

Neither produces an error. Both produce a complete, professional-looking result that is wrong by a factor you would have to already suspect in order to notice. So the sweep generator asserts the code and the unit system on every single file it writes, and the first thing I check on any new batch is that one configuration, run through the automation, matches the same configuration built by hand in the interface. If those two disagree, nothing else in the batch is worth reading.

That check costs ten minutes per batch and it is the reason I am willing to put my seal on numbers that came out of a script. The automation runs the arithmetic. Deciding that the arithmetic is answering the right question is still the engineer's job, and there is no version of this where that changes.

If you have a repeated anchorage condition, an equipment line that mounts to concrete in many configurations, or a design that keeps failing by a small margin, the range is usually more useful than the answer. That work sits inside my [analysis automation practice](/sap2000-ai-automation/).

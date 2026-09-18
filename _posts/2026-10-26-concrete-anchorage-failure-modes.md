---
layout: article
title: "Why Anchors Fail, and Which Failure Decides the Design"
description: "Anchorage to concrete has six or seven distinct failure modes, and the anchor itself is rarely the weakest one. Edge distance, spacing, and whether the concrete is cracked usually decide the answer."
related:
  - "cold-formed-steel"
service_page: "/structural-engineering/"
---

A base plate calculation that checks out perfectly can still fail the anchorage check by a wide margin, and the engineers who are surprised by that are usually thinking about the wrong element. The bolt is a piece of steel with a known strength and a simple calculation behind it. The concrete it is embedded in is the part that decides most designs.

Anchorage to concrete is governed by a set of distinct failure modes that have to be checked separately, in tension and again in shear, and then checked together for combined loading. Each one describes a different way the assembly comes apart, and the governing mode is frequently the one people do not compute.

## The tension failure modes

**Steel failure of the anchor.** The bolt or rod yields and fractures in tension. This is the calculation everyone does first, and it is the one that governs least often.

**Concrete breakout.** A cone of concrete pulls out around the anchor, radiating outward and upward from the embedded end to the surface. The capacity depends on the embedment depth, the concrete strength, and, critically, on how much concrete is actually present around the anchor. An anchor near an edge has a truncated cone, and a group of anchors close together has overlapping cones that cannot each develop their full capacity.

**Pullout.** The anchor slips out of the concrete without taking a cone with it, because the bearing area of the head or the mechanical interlock is not sufficient to develop the concrete. This is the mode that depends most directly on the specific anchor product.

**Bond failure.** For adhesive anchors, the bond between the adhesive and the concrete fails along the length of the embedment. Bond strength varies with the adhesive, with installation conditions including hole cleaning and moisture, with temperature, and with whether the concrete is cracked. It is the mode most sensitive to how carefully the anchor was installed, which is an uncomfortable thing to depend on.

**Side face blowout.** For a deeply embedded anchor close to an edge, the concrete spalls sideways off the face near the anchor head, without a full cone forming. This one governs rarely and is easy to forget entirely.

## The shear failure modes

**Steel failure in shear.** The anchor shears off. Again, straightforward, and again, seldom governing.

**Concrete breakout in shear.** The anchor pushes a wedge of concrete out toward a free edge. This depends heavily on the edge distance in the direction of the shear, and it is the mode that punishes an anchor placed close to the edge of a slab or a pier.

**Pryout.** A short, stiff anchor rotates under shear and levers a piece of concrete out on the side away from the load. It governs for short embedments, which makes it the shear mode that most often surprises people designing a shallow anchorage.

## What actually decides the answer

Three inputs do most of the work.

Edge distance and spacing govern more anchorages than anchor diameter does. The breakout capacity is a function of the volume of concrete available to resist, so moving an anchor an inch further from an edge can do more than going up a bolt size. When a contractor calls to ask whether a larger anchor will solve a failing check, the honest answer is often that a larger anchor makes almost no difference and relocating the anchor makes all of it.

Cracked versus uncracked concrete changes the numbers substantially. Concrete that is cracked in service, which includes most concrete in a tension region under service loads, has lower breakout and bond capacity than uncracked concrete, and the distinction is an explicit input to the calculation rather than a refinement. Assuming uncracked concrete when the section will be cracked is one of the more common ways to produce an unconservative anchorage.

Embedment depth trades against everything else. Deeper embedment increases breakout capacity and reduces pryout, and at some depth the failure mode shifts to steel, which is where you generally want it, because steel failure is ductile and predictable while concrete breakout is neither. Designing so that the anchor governs rather than the concrete is a deliberate objective, and for some structures it is a code requirement rather than a preference.

## Why the base plate calculation misleads

The base plate analysis asks whether the plate can distribute the load and whether the weld and the bolt can take it. It is a steel problem with steel answers, and everything in it is comfortable and familiar. The anchorage asks a completely different question: whether this particular piece of concrete, with this geometry, this edge condition, this reinforcement, and this crack state, can develop the force the steel wants to deliver.

The same disconnect appears in [thin material connections](/articles/cold-formed-steel/), where the limit states belong to the sheet rather than to the fastener. In both cases, the fastener is the thing you specify and the material around it is the thing that fails.

If you have equipment, a sign, a rail, or a base plate that has to attach to existing concrete, the anchorage is worth getting a second look at, particularly if it sits near an edge or in a group. That work falls under my [structural engineering services](/structural-engineering/).

---
layout: article
title: "Does This Abutment Actually Need Seismic Detailing?"
description: "The first question is which framework governs, because AASHTO and Caltrans treat bridge abutments differently. Yielding and nonyielding walls, where Mononobe-Okabe applies, and the conditions under which seismic earth pressure need not be computed at all."
related:
  - "load-combinations"
  - "ground-improvement"
service_page: "/geotechnical-fea/"
---

Somebody asks whether an abutment or a wingwall needs seismic detailing, and the honest first answer is a question back: which design framework governs this project? That is not evasion. The requirements for a bridge abutment in a state that follows the American Association of State Highway and Transportation Officials bridge design specifications differ from the requirements for a comparable structure in California, and the difference is large enough that answering under the wrong framework produces the wrong design.

I hold licenses in states on both sides of that divide, and I have learned to establish the governing framework before anything else.

## The two frameworks ask different questions

The AASHTO bridge design specifications treat seismic demand through an extreme event load combination, with the required level of analysis and detailing scaled to the seismic hazard at the site. Structures in regions of low hazard have limited requirements, and requirements increase with the design acceleration. For retaining structures and abutments, the specification addresses seismic earth pressure and provides conditions under which it can be neglected.

California practice, through the Caltrans seismic design criteria, approaches the abutment differently. The emphasis is on displacement capacity and on the role the abutment plays in the response of the whole bridge, rather than on computing a seismic earth pressure and designing the wall to resist it as a static quantity. A Caltrans abutment is expected to participate in the seismic response, with passive resistance from the backfill mobilized as the superstructure moves into it, sacrificial elements that fail in a controlled way, and seat width sufficient that the span does not lose support if the displacement exceeds the estimate.

Those are genuinely different design philosophies, and they lead to different drawings for the same bridge in the same soil.

## Yielding and nonyielding walls

The technical question underneath most of this is whether the wall can move.

A yielding wall can translate or rotate enough during the event to mobilize an active state in the backfill. A free standing cantilever retaining wall usually can. When the wall can move, the soil behind it partially relieves itself, and the seismic increment of earth pressure is moderate.

A nonyielding wall cannot move enough to relieve. An abutment restrained at the top by the superstructure, particularly an integral abutment, is restrained in exactly this way, and so is a wall braced by a slab. A wall that cannot deflect attracts substantially higher seismic pressure than the active case, by a factor that is not a small refinement.

Getting this classification wrong is the most consequential error in the subject. Applying an active pressure method to a restrained abutment underestimates the demand. Applying a nonyielding solution to a wall that will clearly displace produces an expensive structure designed for a condition that will not occur.

## Where Mononobe-Okabe applies and where it does not

The Mononobe-Okabe method is the classical approach to seismic earth pressure, and it is a pseudo-static extension of Coulomb wedge theory: apply horizontal and vertical accelerations to the failing soil wedge and solve for the resulting thrust.

It is genuinely useful and its assumptions are restrictive. It assumes the wall moves enough to develop an active state, so it does not apply to a nonyielding abutment. It assumes cohesionless backfill, so it does not directly apply to a clay backfill, which admittedly should not be there anyway. It assumes no water in the backfill. And the solution degenerates at high horizontal acceleration combined with a sloping backfill, where the geometry produces an infinite or undefined wedge, which is a signal that the pseudo-static idealization has stopped representing the physics rather than a numerical inconvenience to be worked around.

Selecting the horizontal seismic coefficient is its own decision. The coefficient is derived from the site peak ground acceleration, and the specifications permit a reduced value where a limited amount of permanent wall displacement is acceptable, on the reasoning that a wall that moves an inch has relieved the load that a rigidly held wall would have to resist. Taking that reduction is legitimate and it is also a commitment: it means accepting that the wall will displace, which has to be acceptable to the structure above it.

## When you can skip it

The provisions in both frameworks include conditions under which a seismic earth pressure check is not required, generally combining a low enough design acceleration with a wall that is free to displace without consequence. Many ordinary wingwalls in low hazard regions fall into that category, and a great deal of effort gets spent computing pressures for structures that the governing specification does not require to be checked at all.

I am deliberately not reproducing the numerical thresholds here, because they differ between frameworks, they change between editions, and the version that governs your project is the one in the specification your owner has adopted rather than the one in my memory. The point is that the exemption exists and it is worth confirming before doing the work.

Two conditions remove the exemption regardless. A site classified as requiring a site specific response analysis, which includes sites with liquefiable soils, sensitive clays, or deep soft deposits, cannot use the simplified spectrum at all, and the seismic demand has to come from an actual site response study. And a wall retaining soil that will liquefy is a different problem entirely, where the earth pressure question is secondary to whether the soil will support anything.

## The order I work in

Establish the governing framework. Classify the wall as yielding or nonyielding based on how the structure above it actually restrains it, since the name given to the wall type does not settle the question. Check whether the exemption applies. Confirm the site class and whether a site specific analysis is required. Only then compute anything.

That sequence connects to the point I made about [load combinations](/articles/load-combinations/): the decisions that determine whether the analysis is answering the right question all get made before the analysis runs. It also connects to [ground improvement](/articles/ground-improvement/), because a site with liquefiable backfill or foundation soil often has an economical answer that involves treating the soil rather than designing the wall for the consequences.

If you have an abutment, a wingwall, or a retaining structure and you are not certain whether seismic detailing is required, that determination is usually a short piece of work and it is part of my [geotechnical services](/geotechnical-fea/).

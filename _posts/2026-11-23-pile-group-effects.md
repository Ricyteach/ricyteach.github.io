---
layout: article
title: "Piles Get Weaker When You Put Them Close Together"
description: "A pile in a group resists less lateral load than the same pile standing alone, because its neighbors have already disturbed the soil it depends on. How p-multipliers represent that, and when a single pile analysis stops being adequate."
related:
  - "laterally-loaded-piles"
  - "ground-improvement"
service_page: "/geotechnical-fea/"
---

In the article on [laterally loaded piles](/articles/laterally-loaded-piles/) I mentioned in passing that piles placed close together resist less load per pile than an isolated pile does, and that the effect is represented with p-multipliers. That sentence deserves an article of its own, because the reduction is larger than most people expect and because deciding when it matters is a judgment that has to be made before the analysis is set up.

## Why proximity costs capacity

A laterally loaded pile works by pushing on the soil in front of it. The soil resists, deflects, and eventually yields, and the relationship between how far the pile has moved and how hard the soil pushes back is the p-y curve that the whole analysis depends on.

That resistance assumes the soil in front of the pile is undisturbed and fully confined. When a second pile sits directly behind the first, in line with the direction of loading, the soil that the trailing pile needs to push against has already been displaced and loosened by the leading pile moving through it. The trailing pile arrives at a zone of soil that has been used. It gets less resistance for the same deflection, which means it attracts less load and deflects further.

The effect is usually described as shadowing, and the picture is reasonably intuitive: the leading pile casts a shadow of disturbed soil, and everything behind it stands in that shadow. Piles side by side, perpendicular to the loading direction, interfere much less, because they are not pushing into each other's displaced soil. This is why pile group behavior depends on the direction of loading relative to the group geometry, and why a group can be substantially stronger one way than the other.

## How p-multipliers represent it

The practical treatment is to reduce the soil resistance for each pile by a factor applied to the p-y curve. A leading row might use a value near unity, while trailing rows use progressively smaller values, with the reduction increasing as spacing decreases. At wide spacing the multipliers approach one and the group behaves as a collection of independent piles. At close spacing the trailing rows can lose a substantial fraction of their resistance.

The multipliers are empirical, derived from full scale and model testing, and they vary with soil type as well as with spacing and row position. Values are published in the literature and built into the analysis software, and selecting them is one of the inputs that deserves attention rather than acceptance of a default.

This is a reduction in soil resistance rather than in pile strength. The piles are unchanged. What changes is how much help each one gets from the ground, and therefore how the group distributes load among its members and how far the whole assembly moves.

## The cap changes the problem

A single pile analysis asks how one pile responds to a force and a moment applied at its head. A group analysis asks a different question, because the piles are connected by a cap that enforces compatibility between them.

If the cap is rigid, every pile head moves together: the cap translates and rotates as a unit, and each pile takes whatever load corresponds to its own stiffness at that common displacement. Stiffer piles attract more load. Piles further from the center of rotation take larger axial forces as the cap rotates, so an overturning moment on the group becomes a push and pull couple in the outer piles rather than bending in each pile individually. That mechanism is frequently the dominant way a group resists overturning, and it does not exist at all in a single pile model.

Pile head fixity matters more in a group for the same reason. A pile rigidly connected to the cap develops a moment at its head that a pinned connection does not, which changes both the maximum moment in the pile and the stiffness the cap sees. Battered piles complicate it further, because an inclined pile resolves lateral load partly into axial load, and a group with batter can be much stiffer laterally than the same group driven vertically.

## When a single pile analysis is enough

A single pile analysis is adequate when there is one pile, which is a more common situation than it sounds. Sign foundations, light poles, sound wall posts, and many small structures are supported on a single drilled shaft, and for those the single pile model is the complete and correct model.

It is also adequate when piles are far enough apart that interaction is negligible, which in most guidance means center to center spacing of roughly six diameters or more in the direction of loading, with the threshold lower for spacing perpendicular to the load. Beyond that spacing, treating the piles independently and dividing the load among them is defensible.

It stops being adequate when spacing is close, when the group is large enough that trailing rows carry a meaningful share of the demand, when the cap is stiff enough to redistribute load between piles of different stiffness, or when the design is controlled by deflection rather than by strength. That last case is the one that catches people, because group deflection can exceed the single pile prediction considerably even when every individual pile is comfortably within its capacity.

## Where this sits in a site investigation

Group effects depend on soil that has been disturbed by installation, which connects this subject to [ground improvement](/articles/ground-improvement/) in a way worth noticing. Both are concerned with the state of the soil rather than with its state in an undisturbed sample, and in both cases the analysis is only as good as the honesty of the soil parameters going in.

For a group, that means the geotechnical report needs to support not just strength parameters but the stiffness behavior the p-y curves depend on, and it means asking whether the installation method will densify or loosen the soil between the piles. Those questions belong in the scope before the analysis rather than after it.

Pile group analysis is part of my [geotechnical finite element services](/geotechnical-fea/), and the question of whether a project needs it is usually answerable in a short conversation.

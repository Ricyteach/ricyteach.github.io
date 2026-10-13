---
layout: article
title: "Wind on Structures That Are Mostly Air"
description: "Carports, canopies, sports netting, signs, and ground-mount racking fall under wind provisions that most engineers use rarely. How the loading standard classifies an open structure, and why uplift usually decides its design."
related:
  - "load-combinations"
  - "laterally-loaded-piles"
service_page: "/solar-racking/"
---

A carport is a roof on posts. A shade canopy is a fabric panel on a frame. A sports netting system is a row of tall poles with a net between them. A ground-mount solar array is a tilted plane of panels on a rack with open air above, below, and around it. Each of these structures is mostly air, and each of them is designed for wind first.

The wind provisions most structural engineers use every day are written for enclosed buildings: walls, a roof, and a body of air inside. Open structures are covered by different provisions in the same standard, and habits formed on enclosed buildings lead to errors when they are applied to a structure the wind passes through.

## The standard classifies the structure first

The loading standard adopted by most building codes in the United States is ASCE 7, published by the American Society of Civil Engineers. The edition that applies to a project is the one adopted by the jurisdiction where the structure is built, and jurisdictions adopt new editions at different times. The wind procedures have changed between editions, including new provisions for solar arrays, so the edition is the first thing to establish.

For buildings, the standard first asks how enclosed the structure is. An enclosed building has walls with limited openings. A partially enclosed building has a large opening concentrated in one wall, which lets the wind pressurize the interior. An open building has walls that are mostly open on every side, and the 2016 and later editions add a partially open category for buildings that meet none of the other three definitions. A carport or a pavilion with a roof and no walls is an open building, and its roof is treated as a free roof with its own set of coefficients.

Structures that are not buildings at all, such as freestanding signs, solid freestanding walls, open signs, lattice frameworks, and towers, fall into a separate category of other structures. They are designed with force coefficients applied to their projected area, and the coefficients depend on the shape and proportions of the structure.

Applying enclosed building coefficients to an open structure gives a wrong answer, and the error is unconservative for some members and conservative for others. Only the analysis for the correct category shows which.

## Wind acts on both faces at once

On an enclosed building, the standard computes external pressure on the outer face of a wall or roof and internal pressure on the inner face, and then combines them.

A canopy roof or a sign panel has two outside faces. Wind passes over and under a canopy at once, and the net pressure on the roof can act downward or upward depending on wind direction, roof slope, and what is beneath it. The coefficients for open structures are net coefficients that already include both faces. Adding an internal pressure to them, out of habit from enclosed buildings, adds a load the standard does not apply.

The standard also distinguishes between clear flow under a free roof and obstructed flow, where stored material or other objects block the space beneath. A canopy over an empty slab and the same canopy over stacked material are different wind problems.

## Smaller areas see higher pressure

Gusts are local, so a small area can see a short, intense peak pressure that the whole structure never experiences at once.

For components and cladding, meaning the elements that receive the wind directly, the standard accounts for this through the effective wind area, which is approximately the area of the structure that loads a given element. A single purlin, a panel clamp, or a fastener has a small effective wind area and is designed for a higher pressure. Main frames and foundations are designed under the provisions for the main wind force resisting system, which give lower average pressures over the whole roof. Edges and corners of a free roof also see higher pressure than its middle. Designing a clamp with the main frame pressures underestimates the load on the clamp, and designing the frame with the clamp pressures makes every member heavier than necessary.

## Solidity: how much of the outline is solid

For a net, a lattice, or an open sign, the wind acts on the solid material only. The solidity ratio is the solid area divided by the gross area inside the outline. The force coefficient for an open sign or a lattice framework depends on its solidity and on whether its members are flat or rounded.

The solidity used in a calculation has to come from the actual product. A windscreen, a banner, or a privacy screen attached to a net or a fence turns that area into a solid panel, and the structure has to be designed for that condition if it can occur.

## Light structures are designed by uplift

A carport or a solar rack weighs very little compared with the wind force on it. When the net wind force acts upward, the self weight is the only gravity load counteracting it, and the load combinations in the standard count that weight at a reduced value for exactly this check, as described in the article [The Load Combination Is the Design](/articles/load-combinations/). On light open structures, the uplift combination with minimum dead load usually decides the connections, the anchorage, and the foundation.

The foundation for an open structure is usually a pier or an embedded post with a small vertical load and a large overturning moment from wind. That is a lateral load problem, the one described in the article [How a Pile Resists a Sideways Shove](/articles/laterally-loaded-piles/), and the depth of the pier is usually set by the lateral resistance of the soil, by how far the pier may deflect, and by the uplift it has to resist.

## What this means for a fabricator or an installer

If you sell or install carports, canopies, netting, signs, or ground-mount racking, the wind calculation for your product should state which category of structure it assumes, which edition of the standard it follows, which flow condition and solidity it uses, and which load combination governs each element. Those items are where I start any review of an open structure. Wind on open structures is part of my [solar racking engineering](/solar-racking/), which covers carports and ground-mount systems as well as rooftop arrays.

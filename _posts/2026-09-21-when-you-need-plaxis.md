---
layout: article
title: "When Do You Actually Need PLAXIS?"
description: "PLAXIS is powerful and frequently unnecessary. When established hand methods are the right answer, when genuine soil-structure interaction demands finite element analysis, and why the inputs matter more than the output."
related:
  - "what-is-cande"
  - "ground-improvement"
  - "laterally-loaded-piles"
service_page: "/geotechnical-fea/"
---

PLAXIS is a geotechnical finite element program, in 2D and 3D versions, that models soil as a continuous material with realistic stress-dependent behavior, together with the structures in and on it, the groundwater, and the sequence in which everything gets built. It is a powerful tool and I use it regularly. It is also frequently the wrong tool, and an honest engineer will tell you when you do not need it, because a full FEA on a problem that does not call for one is a way to spend your money making a simple answer look complicated.

## When you do not need it

Most routine geotechnical questions have been solved with closed-form methods, design charts, and limit-equilibrium analysis for decades, and those methods are not inferior, they are appropriate. Bearing capacity of a spread footing, settlement of a simple foundation on reasonably uniform soil, the stability of a straightforward slope: these are well served by established hand methods and dedicated slope-stability tools. Reaching for finite element analysis on any of them adds cost and the appearance of rigor without adding real understanding. If your problem fits in a chart, use the chart.

## When you do need it

PLAXIS earns its keep when the problem has interactions that simpler methods cannot represent honestly.

The clearest case is genuine soil-structure interaction: a deep excavation with bracing or tieback anchors, a tunnel, a complex retaining system, an integral abutment, anything where the soil and the structure push on each other and the answer depends on their combined stiffness. The second case is deformation. Limit-equilibrium analysis gives you a factor of safety against failure, but it cannot tell you how much something will move. When the design is controlled by tolerable settlement or wall deflection rather than by collapse, you need a method that computes displacements, and that is finite element territory. Staged and time-dependent problems are the third: an embankment built in lifts over soft ground, consolidation settlement developing over months or years, loads applied in a sequence that matters. And slope problems with complicated geometry, layered strata, pore pressures, or reinforcement often outgrow the limit-equilibrium model and need the continuum.

## The part that separates good FEA from confident nonsense

The danger of a tool like this is that it will always produce a result, beautifully rendered, whether or not your inputs deserve to be believed. The skill is in the soil constitutive model and its parameters. A simple Mohr-Coulomb model is fine for some problems and badly misleading for others, where a Hardening Soil model or another advanced formulation is needed to capture how stiffness changes with stress and strain. Choosing the model and justifying the parameters, ideally against the actual soil data, is the engineering. The software is just the calculator.

## How this fits with the rest of the toolbox

PLAXIS is general-purpose geotechnical FEA, which is a different thing from [CANDE](/articles/what-is-cande/), the specialized finite element tool for buried structures. They overlap in spirit and almost never in application, and part of scoping a job correctly is knowing which one the problem actually wants. It also pairs naturally with the geotechnical work I have written about elsewhere: you might model [improved ground](/articles/ground-improvement/) directly to predict its settlement, or run a continuum analysis to back up a [laterally loaded shaft](/articles/laterally-loaded-piles/) in unusual soil.

If someone has told you your project needs finite element geotechnical analysis, it is worth confirming that it really does. Sometimes the answer is yes and it is exactly the right investment. Sometimes the answer is that a chart and an afternoon will do, and I would rather tell you that. Either way, this falls under my [geotechnical FEA services](/geotechnical-fea/).

---
layout: article
title: "How a Pile Resists a Sideways Shove"
description: "Lateral load controls most sign and pole foundations. Why hand calculations fall short, how LPile and GROUP solve the nonlinear beam-on-springs problem, and when you need each."
related:
  - "teaching-ai-file-formats"
  - "what-is-cande"
service_page: "/geotechnical-fea/"
---

Most people picture a pile or a drilled shaft as something that carries weight straight down: a column driven into the earth to reach firm material. That is half the job. The other half, and often the harder half to analyze, is resisting load that pushes sideways. A tall sign on a single shaft, a sound wall, a traffic signal, a light pole, a mast: these put relatively little vertical load on their foundation and a large horizontal force and overturning moment. The governing question is whether the foundation will tip, and how far it will lean on the way there.

## Why a hand calculation falls short

The reason lateral pile behavior is genuinely hard is that the soil resistance is nonlinear and depends on how far the pile has already moved. Push the shaft a little and the soil pushes back gently. Push it further and the resistance grows, but only up to a limit, after which the soil yields and gives no more. That relationship between soil pressure and pile deflection, the p-y curve, is different for soft clay, stiff clay, sand, and weak rock, and it changes with depth.

So the real model is a beam embedded in a bed of nonlinear springs, where every spring has its own force-deflection law. The pile bends, the springs resist according to how much each one has deflected, and the whole system has to find equilibrium. That is not a closed-form calculation. Simplified rigid-pile methods such as Broms exist and are useful for checking the order of magnitude, but layered soils, flexible shafts, and combined axial and lateral loading demand the full nonlinear solution.

## The tools, and why there are two

This is solved with software built specifically for the problem. For a single pile or shaft I use LPile, from Ensoft, which solves the nonlinear beam-on-springs system and returns deflection, bending moment, and shear along the full depth of the shaft. The p-y curves come from established models built into the program: Matlock for soft clay, Reese for stiff clay and for sand, and dedicated formulations for weak rock, selected from the soil report.

When piles are grouped close together, a second effect appears: each pile disturbs the soil that its neighbors depend on for support, so the group is weaker per pile than an isolated one, an effect represented with p-multipliers. That is the purpose of GROUP, also from Ensoft, which analyzes the group as a system instead of treating each pile as though it acted alone. Knowing when a problem needs GROUP instead of LPile is part of doing the work correctly.

## A worked example you can picture

A pylon sign on a single drilled shaft is the cleanest illustration. The wind load on the sign face, taken from ASCE 7, acts high above grade and produces a large overturning moment at the foundation. The axial load is negligible. You take the soil parameters from the geotechnical report, build the shaft in LPile, and read off how deep it has to go and how much reinforcement it needs so that deflection stays tolerable and the concrete section, designed to ACI 318, can carry the bending. For transportation structures the load and resistance side shifts to AASHTO LRFD, and the underlying p-y method is the same. I have done exactly this kind of pylon foundation more than once, and the shaft length and reinforcement are almost always determined by the lateral analysis.

## The companion to a tool I already wrote about

I have written before about [teaching a language model to generate LPile input files reliably](/articles/teaching-ai-file-formats/). That article was about the file format. This one is the engineering reason you run LPile in the first place. The automation makes the input quick to produce. The judgment about p-y models, group effects, and whether the answer is physically believable is the part that still requires an engineer, and always will. Lateral pile analysis is one part of a broader [geotechnical finite element practice](/geotechnical-fea/) that also covers soil-structure interaction for [buried structures](/articles/what-is-cande/) and continuum analysis for more complex site problems.

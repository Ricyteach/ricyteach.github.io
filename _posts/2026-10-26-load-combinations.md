---
layout: article
title: "The Load Combination Is the Design"
description: "The most consequential decisions in a structural analysis are made before the analysis runs, when you decide which load cases exist and how they combine. Most combination errors never appear in the output."
related:
  - "where-is-the-neutral-axis"
  - "concrete-anchorage-failure-modes"
service_page: "/structural-engineering/"
---

Ask an engineer what the hard part of an analysis was and you will usually hear about the model: the geometry, the connections, the element types, the soil springs. Those are the visible decisions. The decisions that more often determine whether the answer is right were made earlier, when someone decided which load cases exist and how they combine.

A structural model is a machine for turning loads into forces. If the loads going in are the wrong set, every number that comes out is wrong in a way the model cannot detect, because the model has no opinion about which loads should have been applied.

## Strength design and allowable stress design are different questions

The first decision is which design philosophy governs, and it is not a matter of preference.

Strength design, also called load and resistance factor design, multiplies the loads up by factors that reflect how much each one might exceed its nominal value, and compares the result to a reduced member capacity. Allowable stress design combines the loads at or near their nominal values and compares the result to a capacity divided by a safety factor. The two use different combinations, different factors, and produce different governing cases.

Mixing them produces results that look reasonable and are meaningless. A foundation designed with strength level loads against an allowable bearing pressure is oversized by roughly the load factor, and a member checked with service loads against a factored capacity is unconservative by the same amount. Both mistakes are easy to make on a project where the structural design is by one method and the geotechnical report is written for the other, which is most projects.

## Dead load helps and hurts

The single most common bookkeeping error I see is treating dead load as a fixed quantity.

Dead load is favorable in some combinations and unfavorable in others. When the governing effect is downward, more dead load increases the demand, and the combination applies a factor greater than one. When the governing effect is uplift or overturning, dead load resists the demand, and the combination applies a reduced factor, because the code is asking what happens if the structure weighs less than you assumed. A sign foundation, a canopy, a rooftop array, and a light pole base are all designed by the combination where the dead load is minimized.

This means dead load needs both a maximum and a minimum treatment, and the two produce different governing members within the same structure. A model run with a single dead load case and a single factor gives the right answer for half the structure.

The same logic applies to lateral earth pressure and to groundwater. Soil that resists sliding on one side of a wall is favorable and gets a minimum treatment. Soil that drives the wall is unfavorable and gets a maximum. The two cannot both be present at their extreme values, and deciding which combination is physically possible is engineering rather than bookkeeping.

## Wind is a family of cases

Wind loading in current practice is a set of cases covering the directions the wind can come from, combined with an internal pressure that can act in either direction.

For an enclosed building, the internal pressure is applied as a positive and a negative case, and both have to be carried through every wind direction, because the governing case for a roof member under net uplift is generally wind in one direction combined with internal pressure pushing outward. Dropping one half of that pair is invisible in the output and unconservative for the members that are governed by it.

Directionality adds more cases. A rectangular structure has wind cases for each principal direction, and for many structures the code requires combinations with wind acting simultaneously along both axes at reduced magnitudes, which represents oblique wind. Open structures, the category that includes carports, canopies, and freestanding racking, use an entirely different set of pressure coefficients from enclosed buildings, and applying enclosed building coefficients to an open structure is a mistake that produces low loads.

## Snow is rarely uniform

Balanced snow is the easy case and rarely the governing one. Drifted snow against a parapet or an adjacent taller structure, unbalanced snow on a gable or a curved roof, and sliding snow from an upper roof onto a lower one all produce concentrated loads several times the balanced value over part of the span. A member designed for balanced snow alone can be substantially undersized at one end.

## Seismic carries its own arithmetic

The seismic load in a combination is not simply the horizontal force from the analysis. It is that force multiplied by a redundancy factor that depends on how much of the lateral system would be lost if one element failed, combined with a vertical component proportional to the design acceleration and the dead load, applied both upward and downward.

Separately, certain elements are designed for an overstrength level force rather than the ordinary seismic force, because the intent is that those elements stay elastic while the ductile elements yield. Collectors, some connections, and anchorage to concrete frequently fall into that category. Using the ordinary seismic load where the overstrength load is required is a code compliance failure that no analysis output will flag.

## Why these errors survive review

Every error described above shares a property: it produces a complete, internally consistent set of results. The model converges. The plots look correct. The member checks report ratios. Nothing anywhere in the output says that the combination set was missing a case.

That is why I treat the combination list as a deliverable in its own right, written out explicitly and reviewed before the model runs, rather than as a setup step to get past. The same first principles habit that makes the [neutral axis question](/articles/where-is-the-neutral-axis/) tractable applies here: know exactly what you are asking the analysis to compute, and why. That discipline is part of every project under my [structural engineering services](/structural-engineering/).

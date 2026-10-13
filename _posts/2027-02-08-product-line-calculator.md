---
layout: article
title: "One Calculator for an Entire Product Line"
description: "A company that sells carports, racking, signs, or netting in many jurisdictions needs a design for every order. What a calculator for a whole product line has to bound, how it is validated, and why it refuses some inputs."
related:
  - "calculator-as-deliverable"
  - "wind-open-structures"
service_page: "/solar-racking/"
---

A company that sells carports, solar racking, signs, or sports netting sells the same structure many times with different numbers. Every order arrives with its own site, its own dimensions, and its own building department. Each one needs a design that is correct for that site and that the building department will accept.

The article [Sometimes the Calculator Is the Deliverable](/articles/calculator-as-deliverable/) described the general idea: do the engineering once, thoroughly, and capture it in a tool that produces a correct design for any valid set of inputs. This article covers what that takes for an entire product line, where the inputs come from every jurisdiction the company sells into. I have built calculators of this kind, including a sign foundation calculator for a sign company, with a continuous trench footing option alongside the drilled shaft, and a carport calculator with a standard drawing for a carport company.

## The input space is a product of two lists

The first list is the site conditions. The second is the configuration options the company offers. Every combination of a site and a configuration is a design the calculator might be asked for.

The site conditions include the wind speed, the exposure category, which describes the roughness of the terrain upwind of the structure, the ground snow load, and the seismic parameters. Some products add the soil bearing pressure and the frost depth at the site. The configuration options include the span, the height, the bay count, the tilt angle, the panel or sign face size, the post size, and whatever accessories change the loads, such as a windscreen on a net or a solid end wall on a carport.

The code edition belongs on the first list. Each jurisdiction adopts an edition of the building code and, through it, an edition of ASCE 7, the loading standard published by the American Society of Civil Engineers. Jurisdictions adopt new editions at different times, and the procedures differ between editions, including the wind provisions for open structures described in the article [Wind on Structures That Are Mostly Air](/articles/wind-open-structures/). A calculator that treats the edition as a constant is correct only in the jurisdictions that happen to use that edition. A product line calculator should take the edition as an input and apply the procedure for the edition selected. Local amendments, special wind regions, and local snow requirements are jurisdiction inputs of the same kind.

## Bounding each input

Each input has a range that the calculator is designed for, and the ranges are engineering decisions. A wind speed range is set by the markets the company sells into. A span range is set by the products the company builds. A soil bearing range is set by the soil conditions the foundation design can address without a site investigation.

The bounds also cover combinations. A tall structure with a long span in the highest wind speed and the most open exposure might fall inside every individual range and still be a configuration the structural system cannot support. The calculator has to recognize those combinations as well as the individual limits.

## Validating at the corners

A calculator is most likely to be wrong at the corners of its input space, where the governing check changes. At low wind speeds and heavy snow, a carport frame is governed by downward load on the beams. At high wind speeds in open terrain, the same frame is governed by uplift at the foundation. Somewhere in between, the governing check switches from one to the other, and a mistake in either check appears only where that check governs.

Testing a calculator with typical inputs in the middle of the range exercises the checks that govern there and leaves the others untested. For that reason, the validation should be concentrated at the corners: the highest wind with the lowest dead load, the heaviest snow with the longest span, the tallest configuration with the weakest soil, and each code edition the calculator supports. At each corner, the calculator result should be compared with an independent analysis built from first principles, and the two have to agree.

This is the same approach described in the article [A Hundred Anchor Configurations Instead of One](/articles/automating-anchor-checks/), where a sweep across embedment, edge distance, and anchor diameter shows where a design passes and how close it is to failing. A product line calculator applies that idea to an input space with more dimensions. Analysis automation makes validation at this scale practical, since the independent models that check the corners can run as a batch that the engineer sets up and then reviews.

## Refusing what it was not designed for

A calculator that accepts any input will eventually produce a design for a case its author never considered, and that design will look exactly as authoritative as a correct one. For that reason, the calculator should refuse inputs outside its envelope. It should stop and state which input is out of range, and the order then goes to an engineer for an individual design.

The refusal is part of the engineering. The envelope is the extent of what the engineer has checked and is professionally responsible for, and the calculator should produce no design outside it.

## Who is responsible

A licensed engineer has to direct the building of the calculator, decide its bounds, build and review the independent analyses used to validate it, and accept professional responsibility for the designs it produces within its envelope. The automation runs the arithmetic and the validation batches. The engineering judgment about which checks apply, which inputs are allowed, and whether the results agree belongs to the engineer.

Each design the calculator produces still has to be signed by an engineer licensed in the state where the structure is built. A calculator is therefore issued only for the states where the signing engineer holds a license, and each output is reviewed by that engineer before it is signed.

Each version of the calculator should be fixed and documented. When a code edition changes, a product changes, or the company enters a new market, the calculator should be updated, revalidated at its corners, and issued as a new version, with the designs produced by the earlier version traceable to it.

If you sell carports, racking, signs, or netting into many jurisdictions and you are paying for the same analysis on every order, a calculator for the whole product line may be the more economical arrangement. That work is part of my [solar racking engineering](/solar-racking/) and extends to the other open structures described here.

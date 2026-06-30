---
layout: article
title: "What CANDE Is, and When You Actually Need It"
description: "Plain-English explanation of what CANDE is, when buried pipe and culvert work actually needs soil-structure interaction analysis, and what the program does and does not do."
---

If someone has told you a buried pipe or culvert needs a "CANDE analysis" and you are not sure what that means or whether you really need one, this is the plain-English version.

## The short answer

CANDE stands for Culvert ANalysis and DEsign. It is a finite element program built specifically for buried structures: pipes, culverts, and arches with soil over and around them. It came out of work for the Federal Highway Administration, and it has been the standard tool for soil-structure interaction on buried structures for decades. Unlike general structural software, it is built around one idea: a buried structure and the soil around it act together, and you cannot understand one without the other.

## Why a buried pipe is not just a beam

The intuitive way to analyze a pipe is to treat it like a ring or a beam, push a load on top, and see what happens. For a buried structure that approach is either badly wrong or wildly conservative, because it ignores the soil.

When a flexible pipe deflects under load, it pushes outward against the soil at its sides, and that soil pushes back. That side support is often what holds the structure up. A rigid pipe does the opposite, attracting load to itself because it is stiffer than the soil around it. Either way, the soil is not just load sitting on top of the structure. It is part of the structural system. CANDE models the soil and the structure together, which is the entire point.

## When you actually need it

You need this kind of analysis when the soil-structure interaction genuinely drives the answer. In practice that means large-diameter culverts and pipes, deep fill heights, shallow cover under live load, unusual installation conditions, and any time the structure is flexible enough that side support matters. It applies across materials: corrugated metal, reinforced concrete, thermoplastic, and fiberglass, along with metal and concrete arches.

You probably do not need it for a small-diameter pipe under modest cover in standard conditions, where established tables and simpler methods are perfectly adequate and a full finite element model is overkill. Part of the value of asking is finding out you do not need to spend the money.

## What it does, and what it does not

CANDE models construction in stages, building up the soil in layers the way it actually gets placed, because a buried structure sees load incrementally during installation, not all at once at the end. It uses soil models that capture how soil stiffness changes with stress and confinement. It will give you deflections, thrusts, and moments through the structure under realistic conditions.

What it does not do is make judgment calls for you. The soil properties, the installation assumptions, the interpretation of the results: those are engineering, and the program is only as good as the inputs and the person reading the output. A buried-structure analysis that does not interrogate its own soil assumptions is not worth much.

## Who I am writing this for

I do a fair amount of buried-structure work, and a lot of it comes from smaller outfits who have an occasional culvert or pipe problem and no reason to keep a soil-structure interaction specialist on staff. If that is you, this is exactly the kind of thing I am happy to take on, including the small jobs that larger firms tend to decline.

One last note, since it is relevant: the manual side of preparing these models, assigning materials and construction steps across a mesh, got tedious enough that I eventually built my own preprocessor to handle it. [That is a story for another article.](/articles/cande-editor/)

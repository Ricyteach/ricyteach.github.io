---
layout: article
title: "The Signature Curve"
description: "The finite strip analysis behind the Direct Strength Method produces one plot for a cold-formed steel section. How to read its local, distortional, and global regions, what changes the curve, and what it leaves to the strength equations."
related:
  - "distortional-buckling-dsm"
  - "cold-formed-steel"
service_page: "/structural-engineering/"
---

[The Buckling Mode Hot-Rolled Intuition Misses](/articles/distortional-buckling-dsm/) described the three ways a cold-formed steel member buckles, which are local, distortional, and global, and mentioned the finite strip analysis that supplies the elastic buckling loads for the Direct Strength Method. This article covers that analysis and the plot it produces, which is called the signature curve.

## What the finite strip method computes

The finite strip method divides the cross-section into narrow strips that run the full length of the member. Across the section, the deformation of each strip is described by the displacements and rotations at its two edges. Along the length, the deformation is assumed to follow a sine curve of a chosen half-wavelength, meaning the distance along the member between two points of zero buckling displacement.

The engineer applies a reference stress distribution to the section: uniform compression for a column, or a linear distribution from compression to tension for a beam in bending. For one half-wavelength, the analysis solves for the factor by which that reference stress must be multiplied to cause elastic buckling, along with the shape of the buckled section at that load. Repeating the solution across a range of half-wavelengths produces the signature curve.

The tool I use is a finite strip elastic buckling solver that is a validated port of the Constrained and Unconstrained Finite Strip Method (CUFSM) program, the standard program for this analysis. It writes files that the original CUFSM program can open for plotting.

## Reading the curve

The horizontal axis is half-wavelength, usually on a logarithmic scale. The vertical axis is the buckling load factor, which converts directly to a buckling load or moment. For a typical lipped channel in compression, the curve has three regions.

At short half-wavelengths there is a first minimum. This is local buckling. The flat plate elements of the section ripple in short waves while the corners and fold lines stay straight. The half-wavelength at this minimum is on the order of the width of the most slender flat element, typically less than the depth of the web, and the load at the minimum is the local critical load.

At intermediate half-wavelengths there is a second minimum. This is distortional buckling. The flange and its lip rotate together about the junction of the flange and the web, and the web bends to allow that rotation, so the shape of the cross-section changes. The half-wavelength is several times longer than the local one, and the load at this minimum is the distortional critical load.

At long half-wavelengths the curve descends steadily without a minimum. This branch is global buckling, in which the whole member bends, twists, or both, while the cross-section keeps its shape. Global buckling has no preferred wavelength, so the global critical load is read at the half-wavelength corresponding to the member's actual unbraced length. In the classical form of the method the ends are simply supported, and the engineer accounts for other end conditions separately. When the unbraced lengths for bending about each axis and for twisting differ, one reading from the curve does not represent all of them, and each is checked separately.

Not every curve is that orderly. A channel without lips has no distortional minimum, and in some sections the local and distortional minima merge. Identifying each mode then requires looking at the buckled shapes. The constrained form of the method, which is the source of the word "constrained" in the program's name, can restrict the deformation to one class of mode at a time so that each critical load can be found separately.

## What changes the curve

The lip is the clearest example. Without a lip, the free edge of a flange is unsupported, and the flange buckles locally at a low stress. A lip stiffens that edge and raises the local minimum. A lip that is too short provides little restraint against rotation of the flange, and the distortional minimum stays low. Lengthening the lip raises the distortional minimum, up to the point where the lip itself becomes a slender plate that buckles locally.

Intermediate stiffeners, the small folds rolled into a wide web or flange, divide a wide plate into narrower ones. Local buckling of a plate depends on the ratio of its width to its thickness, so narrower plates buckle locally at a higher stress. A stiffener can also introduce a distortional mode of its own, in which the stiffener moves out of plane together with the plate around it.

Thickness raises the curve by a different amount in each region. The elastic local buckling stress of a plate increases with the square of the ratio of thickness to width, so a thicker section moves the local minimum up sharply. The distortional minimum also rises with thickness. On the global branch, flexural buckling stress changes little with thickness, since it depends on the overall dimensions of the section. Torsional and flexural-torsional buckling stress rises with thickness, because the resistance of an open section to twisting increases with the cube of its thickness, and that effect is largest at long half-wavelengths.

Lips and stiffeners are placed to raise the buckling stress of particular modes, a point that the article [Cold-Formed Steel Is Not Just Thin Hot-Rolled Steel](/articles/cold-formed-steel/) made when describing why the sections look the way they do.

## What the curve leaves to the strength equations

The signature curve gives elastic buckling loads. Strength is a separate calculation. The Direct Strength Method in AISI S100, the North American specification for cold-formed steel published by the American Iron and Steel Institute, takes the local, distortional, and global elastic buckling loads, together with the load that causes the full section to yield, and returns a nominal strength for each mode. Those equations account for the strength a thin plate retains after it buckles locally, for the smaller reserve after distortional buckling, and for the interaction of local buckling with global buckling.

The analysis also assumes a perfectly straight member, elastic material, the chosen reference stress distribution, and the end conditions of the method. Holes in the web, connections, and concentrated loads at supports are outside the analysis and are addressed separately.

## Directing the analysis

The solver computes the curve. I choose the reference stress for each load case, choose the half-wavelengths at which each critical load is read, confirm from the mode shape that each minimum is the mode it appears to be, and use the results in the strength check. I review every result and remain professionally responsible for the design. Cold-formed steel design of this kind is part of my [structural engineering services](/structural-engineering/).

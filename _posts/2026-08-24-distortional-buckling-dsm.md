---
layout: article
title: "The Buckling Mode Hot-Rolled Intuition Misses"
description: "Cold-formed steel fails in three buckling modes. The third one, distortional buckling, has no hot-rolled analog and governs constantly in thin sections. What it is and how the Direct Strength Method handles it."
---

If you were trained on hot-rolled steel, you carry a mental list of how a beam or column fails: it yields, or it buckles globally, by flexural buckling in a column or lateral-torsional buckling in a beam. Local buckling is on the list too, but for the compact wide-flange shapes that fill the AISC manual it usually does not govern, so it lives at the back of the mind. That list is complete enough for hot-rolled work. It is dangerously incomplete for cold-formed steel, because it is missing a mode that has no real hot-rolled analog and that governs constantly in thin sections: distortional buckling.

## Three modes, not two

Cold-formed members fail in three distinct buckling modes, and the difference between them is about what the cross-section does.

In local buckling, the flat plate elements ripple at short wavelength while the fold lines, the corners and bends, stay put. In global buckling, the whole member translates or twists over its full length while the cross-section holds its shape rigidly. Distortional buckling sits in between, at intermediate wavelength, and it is the one people do not picture: the cross-section itself changes shape. In a typical lipped channel, the flange and its stiffening lip rotate as a unit about the flange-to-web junction, and the web bends to allow it. The section is not rippling and it is not just leaning over. It is distorting.

That intermediate mode is exactly the one hot-rolled intuition has no slot for, and in the thin, lipped, stiffened sections used in cold-formed framing and solar racking it frequently controls the design.

## Why the method you use changes the answer

Here is the part where the code edition matters, and it matters a lot. Cold-formed steel in North America is designed to AISI S100, which is a different specification from the AISC 360 you use for hot-rolled, with a different philosophy built around the reality that local buckling is normal rather than exceptional.

For most of its history, AISI design used the Effective Width Method, which handles local buckling by shaving each plate element down to an "effective" width and computing capacity on the reduced section. The trouble is that the Effective Width Method does not naturally see distortional buckling, and for years it was not explicitly checked at all. That is the trap: an older method, applied without a separate distortional check, can miss the mode that governs.

The Direct Strength Method changed this. It was introduced into AISI S100 in the 2004 edition as Appendix 1, alongside the traditional method rather than replacing it. Instead of effective widths, DSM asks you to compute the elastic buckling load or moment for each mode separately, local, distortional, and global, and feed those into strength curves. In the 2016 edition of S100 the specification was reorganized so that the Direct Strength Method and the Effective Width Method both live in the main body as recognized, co-equal approaches, and that structure carries through the 2020 edition. The practical upshot for anyone working in a modern AISI spec is that distortional buckling is now a first-class limit state with its own check, not an afterthought hiding in an appendix.

## How you actually get the numbers

Computing those elastic buckling loads by hand is not realistic for a real section, so DSM is paired with a finite strip analysis. The standard tool is CUFSM, and I run a Python implementation, pyCUFSM, which produces the signature curve that separates the local, distortional, and global modes and hands DSM the buckling stresses it needs. That coupling, finite strip elastic buckling feeding the Direct Strength Method, is what makes distortional buckling a routine, defensible check instead of a mode you hope does not bite you.

If the [neutral-axis article](/articles/where-is-the-neutral-axis/) was about reading a section's behavior from first principles, this is the same habit applied to stability: know which mode you are actually fighting, and use a method that can see it.

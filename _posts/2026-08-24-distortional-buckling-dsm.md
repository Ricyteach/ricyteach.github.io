---
layout: article
title: "The Buckling Mode Hot-Rolled Intuition Misses"
description: "Cold-formed steel fails in three buckling modes. The third one, distortional buckling, has no hot-rolled analog and governs constantly in thin sections. What it is and how the Direct Strength Method handles it."
related:
  - "where-is-the-neutral-axis"
service_page: "/structural-engineering/"
---

If you were trained on hot-rolled steel, you have a mental list of how a beam or column fails: it yields, or it buckles globally, by flexural buckling in a column or lateral-torsional buckling in a beam. Local buckling is on the list too, but for the compact wide-flange shapes that fill the AISC manual it usually does not govern, so it receives little attention. That list is complete enough for hot-rolled work. It is dangerously incomplete for cold-formed steel, because it is missing a mode that has no real hot-rolled analog and that governs constantly in thin sections: distortional buckling.

## Three distinct modes

Cold-formed members fail in three distinct buckling modes, and the difference between them is what the cross-section does.

In local buckling, the flat plate elements ripple at short wavelength while the fold lines, the corners and bends, remain straight. In global buckling, the whole member translates or twists over its full length while the cross-section retains its shape rigidly. Distortional buckling sits in between, at intermediate wavelength, and it is the one people do not picture: the cross-section itself changes shape. In a typical lipped channel, the flange and its stiffening lip rotate as a unit about the flange-to-web junction, and the web bends to allow it. The cross-section distorts, which is where the mode gets its name.

That intermediate mode is exactly the one hot-rolled intuition has no category for, and in the thin, lipped, stiffened sections used in cold-formed framing and solar racking it frequently controls the design.

## Why the method you use changes the answer

The edition of the specification you are working to changes which checks you are required to perform. Cold-formed steel in North America is designed to AISI S100, a different specification from the AISC 360 used for hot-rolled steel, built around the premise that local buckling is a normal occurrence rather than an exceptional one.

For most of its history, AISI design used the Effective Width Method, which handles local buckling by reducing each plate element to an "effective" width and computing capacity on the reduced section. The trouble is that the Effective Width Method does not address distortional buckling directly, and for years it was not explicitly checked at all. That is the hazard: an older method, applied without a separate distortional check, can omit the mode that governs.

The Direct Strength Method changed this. It was introduced into AISI S100 in the 2004 edition as Appendix 1, alongside the traditional method rather than replacing it. Instead of effective widths, the Direct Strength Method asks you to compute the elastic buckling load or moment for each mode separately, local, distortional, and global, and to use those values in strength curves. In the 2016 edition of AISI S100 the specification was reorganized so that the Direct Strength Method and the Effective Width Method both appear in the main body as recognized, co-equal approaches, and that arrangement continues in the 2020 edition. For anyone working to a current AISI specification, distortional buckling now has its own explicit check.

## How you actually get the numbers

Computing those elastic buckling loads by hand is not realistic for a real section, so the Direct Strength Method is paired with a finite strip analysis. The standard tool is CUFSM, and I run a Python implementation, pyCUFSM, which produces the signature curve that separates the local, distortional, and global modes and supplies the buckling stresses the Direct Strength Method requires. That combination, finite strip elastic buckling feeding the Direct Strength Method, makes distortional buckling a routine, defensible check instead of a mode you hope was not the governing one.

If the [neutral-axis article](/articles/where-is-the-neutral-axis/) was about reading a section's behavior from first principles, this is the same habit applied to stability: identify which mode actually governs, and use a method that evaluates it. Cold-formed steel design is a core part of my [structural engineering services](/structural-engineering/).

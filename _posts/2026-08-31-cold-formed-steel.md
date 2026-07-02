---
layout: article
title: "Cold-Formed Steel Is Not Just Thin Hot-Rolled Steel"
description: "Cold-formed steel is governed by a different specification with a different worldview. The behaviors that have no counterpart in hot-rolled work and that will quietly wreck a design if you import the wrong habits."
related:
  - "distortional-buckling-dsm"
  - "where-is-the-neutral-axis"
service_page: "/structural-engineering/"
---

The most common mistake I see engineers make with cold-formed steel is treating it like a small hot-rolled section: same instincts, same code reflexes, just thinner metal. It is a natural assumption and it is wrong, often in ways that are unconservative. Cold-formed steel is its own discipline, governed by its own specification, and a few of the differences will quietly wreck a design if you import hot-rolled habits.

## Different specification, different worldview

Hot-rolled steel is designed to AISC 360, currently the 2022 edition with 2016 and 2010 still in use depending on your adopted code. Cold-formed steel is designed to AISI S100, the North American Specification. These are not the same document with a thickness adjustment. AISC 360 is built around sections stocky enough that they can usually reach yield, so local buckling is a special case. AISI S100 is built around the opposite premise: the plate elements are thin, they buckle before the section yields, and you almost never get the full gross-section capacity. The entire method is organized around that fact.

## What actually bites you

A handful of behaviors have no real counterpart in routine hot-rolled work.

Local buckling is the normal case, not the exception. The thin flats buckle early, so capacity is governed by post-buckling behavior, handled either by reducing the section to effective widths or, in the Direct Strength Method, by an elastic buckling analysis. I wrote separately about the third mode, [distortional buckling](/articles/distortional-buckling-dsm/), which is the one hot-rolled training leaves out entirely.

Web crippling is a real limit state. A concentrated load or a reaction at a support can crush the thin web locally, a failure you essentially never design against in a hot-rolled beam but routinely check in cold-formed members at bearing points and load points.

Cold work of forming changes the steel. The act of bending the corners raises the yield strength locally, and the specification lets you take credit for it in the right circumstances, which is a tool that simply does not exist in hot-rolled design.

Connections are different. You are working with screws and the occasional weld or bolt in thin material, with tilting, bearing, and pull-out limit states specific to thin sheet, not the bolt-and-weld assumptions baked into hot-rolled detailing.

## The version question is not academic

Which edition of S100 you are on can change how you are required to handle these limit states, so it is worth pinning down. The Direct Strength Method entered S100 in the 2004 edition as an appendix, became fully integrated into the main body alongside the Effective Width Method in the 2016 edition, and that structure continues in the 2020 edition. Your jurisdiction's adopted building code points at a specific S100 edition, so confirm which one governs your project rather than assuming the newest. The conceptual gap between an old effective-width-only approach and a modern Direct Strength approach with an explicit distortional check is exactly the kind of difference that matters.

## A concrete artifact

This is not abstract for me. I built a hat-section calculator that runs the AISI checks across a range of dimensions and loads, precisely so the local and distortional limit states get evaluated correctly every time instead of being eyeballed. Cold-formed sections are shaped the way they are, with lips and intermediate stiffeners, specifically to fight the buckling modes described above, and a tool that respects that does better work than instinct carried over from a different material.

If you have cold-formed work, particularly in racking, framing, or any thin-gauge structure, it deserves an engineer who designs it as cold-formed steel, not as hot-rolled steel that went on a diet. That is part of what I do under my [structural engineering services](/structural-engineering/).

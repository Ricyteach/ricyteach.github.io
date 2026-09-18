---
layout: article
title: "The Calculation Sheet Nobody Wants to Change"
description: "Every engineering office has a calculation sheet built years ago by someone who has left, still in use because it works, untouched because nobody wants to break it. Reading one, changing an input, and sweeping it across a range without rebuilding it."
related:
  - "calculator-as-deliverable"
  - "running-legacy-software"
service_page: "/sap2000-ai-automation/"
---

Every engineering office has one. A calculation sheet, usually in a mathematics package or a spreadsheet, built a decade ago by an engineer who has since left the firm. It produces correct answers. It has been checked against hand calculations and against real projects more times than anyone has counted. Nobody fully understands how it works anymore, and nobody wants to be the person who changes something and finds out later that they broke it.

So it stays. It gets opened, one input gets changed, the answer gets copied into a report, and it gets closed again. It is one of the most valuable assets in the office and it is treated like unexploded ordnance.

## Why rebuilding is the wrong instinct

The engineer's instinct on encountering one of these is to rewrite it properly, in a modern tool, with documentation. That instinct is usually wrong, and it is worth being clear about why.

What makes the old sheet valuable is not its arithmetic. The arithmetic is reproducible in an afternoon. What makes it valuable is that it has been validated against reality over years of use. Every time it produced an answer that a project later confirmed, and every time someone caught a case where it needed a correction and made one, the sheet accumulated a kind of trust that a new implementation does not have and cannot be given quickly.

A rewrite discards that. The new version starts at zero validation, and the only way to establish that it agrees with the old one is to run both across many inputs and compare, which requires the ability to run the old one many times, which is the thing that seemed impossible and is the reason the rewrite was proposed.

So the useful capability is access.

## Reading a sheet without opening it

A calculation sheet stored in a structured file format can be read directly, which means the contents are available without running the software, without a license, and without the sheet's own application taking over a screen.

The first useful thing that enables is inventory. What are the inputs? What does the sheet compute? Which values are entered and which are derived? That distinction is the one that takes the most work, because in most of these formats an entered value and a computed one look similar, and telling them apart means locating the definition structure rather than reading the displayed numbers. Getting it wrong means editing something that was never an input, which produces either an error or, worse, a silently inconsistent sheet.

Once that inventory exists, the sheet stops being opaque. Somebody can ask what a sheet assumes without opening it, and the answer is available in a form that can be put into a report.

The second useful thing is comparison. Two versions of a sheet, saved a few years apart under slightly different names, can be compared directly to see what actually changed between them, which is a question that arises surprisingly often and is otherwise answered by opening both and squinting.

## Changing an input and recomputing

Reading is safe. Recalculating requires running the software, and that is where the [difficulties of driving a program with no scripting interface](/articles/running-legacy-software/) reappear.

For the mathematics package I use most, the automation server allows only one instance, so it refuses to start while an interactive session is open. That is a real constraint rather than a bug, and the automation has to detect the condition and say so plainly instead of failing in a way that looks like the sheet is broken. Run with a hidden window, it does not take the screen or the keyboard, which means a batch can proceed while other work continues.

With that in place, the interesting operation becomes possible: change an input, recompute, read the result, repeat across a range. A sheet that computes one answer becomes a sheet that produces a table.

## What that changes

Three things, in increasing order of value.

A parameter study that used to be an afternoon of opening, typing, and copying becomes a batch and a table. The table goes into the report directly, without anyone transcribing numbers between applications, which removes a transcription error class that is otherwise unavoidable.

A sheet whose valid range was never documented can have its range established empirically. Run it across the inputs, look at where the results stop being sensible, and you know the boundaries of the envelope the sheet actually covers. That is information the office did not have, and it is exactly the kind of boundary definition that a [parametric calculator](/articles/calculator-as-deliverable/) requires before it can be handed to anyone.

And a rewrite, if it is genuinely needed, becomes safe. With the ability to run the old sheet hundreds of times, a new implementation can be validated against it across the whole input space rather than at three test points. The accumulated trust transfers, because it has been demonstrated rather than assumed.

## What I do not do

I do not modify the original sheet. The working copy is a copy, the original stays where it is, and anything I produce states which version of the sheet generated it. A sheet that half the office relies on is infrastructure, and the fastest way to lose the confidence of the people who rely on it is to hand back a version that behaves differently from the one they know.

If your office has a sheet like this, one that everyone uses and nobody will touch, it can usually be read, exercised, and bounded without any risk to the original. That work is part of my [analysis automation practice](/sap2000-ai-automation/).

---
layout: article
title: "Using AI to Check an Engineer's Work, Not Do It"
description: "The most reassuring AI application in engineering is also the simplest: using it to catch inconsistencies in a submittal package, not to design anything."
---

Most of the conversation about AI in engineering is about using it to produce something: a model, a calculation, a drawing. That is real, and I have written about the tools I built to do exactly that. But there is a second use that gets less attention and makes a lot of clients more comfortable, because the machine never touches the design. It only checks it.

## The job of catching mistakes

A big part of engineering review is consistency checking. When a submittal package comes across my desk, a set of drawings, a capacity analysis, the supporting documents, much of the work is verifying that it all agrees with itself. Does the support type called out in the analysis match the one shown on the drawings? Does the code edition referenced in one place match the one used in another? Do the stated capacities actually exceed the demands? Are the same members described the same way everywhere they appear?

None of that is glamorous, and all of it matters, because the errors that cause real problems are usually not exotic. They are mundane inconsistencies that slipped through because a human reviewer was reading a hundred pages and the contradiction was on pages twelve and eighty-seven.

## Where AI is genuinely good

This is a task AI is well suited to, precisely because it is not design. Holding a large, detailed document in view all at once and flagging the places where it contradicts itself is the kind of tireless, literal cross-referencing that people are bad at and machines are good at. Used this way, AI does not decide anything. It surfaces discrepancies for a human to look at. Every flag is a question, not a verdict: this number here does not seem to match that number there, is that intended?

That framing matters. The tool is a second set of eyes that never gets tired and never assumes page twelve and page eighty-seven say the same thing just because they should. It makes me a more thorough reviewer. It does not make the engineering decisions, and it is not the engineer of record. I am.

## Why this should reassure you, not worry you

If the idea of AI in engineering makes you nervous, this is the application to look at first, because the risk profile is inverted from what people fear. The worry about AI is that it will confidently produce something wrong and a human will trust it. In a checking role, the AI is not producing the design at all. It is auditing a design a human already made, and a human reviews every flag it raises. The worst case is a false alarm that costs a few minutes. The upside is catching the quiet inconsistency that would otherwise have shipped.

I use AI on both sides of my practice: to build, with [verified tooling and a licensed engineer on every result](/articles/ai-toolkit/), and to check, as a relentless second reader. The checking side is the one I would point a skeptical client to first, because it is the clearest case of the machine doing what it is good at and the engineer doing what only the engineer can.

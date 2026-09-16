---
layout: article
title: "Using AI to Check an Engineer's Work"
description: "The most reassuring application of artificial intelligence in engineering is also the simplest: using it to catch inconsistencies in a submittal package."
related:
  - "ai-toolkit"
  - "sap2000-ai-tool"
service_page: "/structural-engineering/"
---

Most of the conversation about artificial intelligence (AI) in engineering is about using it to produce something: a model, a calculation, a drawing. That is real, and I have written about [the tools I built](/articles/sap2000-ai-tool/) to do exactly that. There is a second use that gets less attention and makes a lot of clients more comfortable, because the machine never produces the design. It only checks it.

## The job of catching mistakes

A large part of engineering review is consistency checking. When a submittal package arrives for review, a set of drawings, a capacity analysis, the supporting documents, much of the work is verifying that it all agrees with itself. Does the support type called out in the analysis match the one shown on the drawings? Does the code edition referenced in one place match the one used in another? Do the stated capacities actually exceed the demands? Are the same members described the same way everywhere they appear?

None of that is glamorous. The errors that cause real problems are rarely exotic. They are mundane inconsistencies that slipped through because a human reviewer was reading a hundred pages and the contradiction was on pages twelve and eighty-seven.

## Where AI is genuinely good

This is a task AI is well suited to, precisely because it involves no design decisions. Reading a large, detailed document in full and identifying the places where it contradicts itself is the kind of tireless, literal cross-referencing that people are bad at and machines are good at. Used this way, AI decides nothing. It reports discrepancies for a human to look at. Every item it reports is a question: this number here does not seem to match that number there, is that intended?

The tool is a second reader that never gets tired and never assumes page twelve and page eighty-seven agree because they ought to. It makes me a more thorough reviewer. It makes no engineering decisions, and it is not the engineer of record. I am.

## Why this is the safest place to start

If the idea of AI in engineering makes you nervous, this is the application to look at first, because the risk profile is inverted from what people fear. The worry about AI is that it will confidently produce something wrong and a human will trust it. In a checking role, the AI audits a design a human already made, and a human reviews every question it raises. The worst case is a false alarm that costs a few minutes. The benefit is catching the quiet inconsistency that would otherwise have gone out with the package.

I use AI on both sides of my practice: to build, with [verified tooling and a licensed engineer on every result](/articles/ai-toolkit/), and to check, as a relentless second reader. The checking side is the one I would show a skeptical client first, because it is the clearest case of the machine doing what it is good at and the engineer doing what only the engineer can. Both are part of the [structural engineering work](/structural-engineering/) I do.

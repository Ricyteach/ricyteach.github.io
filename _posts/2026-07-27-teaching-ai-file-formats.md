---
layout: article
title: "Then I Did It Again, With an Even Worse File Format"
description: "LPile's input format is deliberately hostile: custom floating-point conventions, inconsistent field separators, and required typos. Teaching an AI to handle it anyway."
related:
  - "sap2000-ai-tool"
  - "cande-editor"
service_page: "/sap2000-ai-automation/"
---

When I wrote about building [an AI tool that writes SAP2000 models](/articles/sap2000-ai-tool/), the central point was that a language model is good at producing structured text but does not know any particular program's input format, and that teaching it one reliably is hard, slow work that demands deep fluency in both the software and the AI. SAP2000 was not the only place I needed that. It was just the first one I wrote about.

## LPile, and why its file format is a special kind of awful

LPile analyzes laterally loaded piles and drilled shafts. It is the standard tool for the job, and like a lot of standard engineering tools it is old, which means its text input format carries decades of accumulated quirk. If SAP2000's format is unforgiving, LPile's is openly hostile.

A few examples, without turning this into a manual. Numbers are written in a floating-point style that standard programming libraries do not produce by default, so you cannot just print a value and move on. The way fields are separated changes from one block of the file to the next, so a parser that works for one section silently mangles another. And in a couple of places the file has to contain the program's own spelling mistakes, exactly, because the software expects them and rejects the corrected version. You read that right. To make the file valid, you have to reproduce a typo.

None of that is in any AI's general knowledge, and none of it is forgiving. A file that is ninety-nine percent right is a file that does not load.

## Why this is not a copy-paste job

People sometimes assume that once you have done this for one program, doing it for the next one is just repetition. It is not. Every one of these formats is its own little universe of rules, conventions, and landmines, and the only way to get a tool that produces valid files every time is to go through the same grinding loop I went through for SAP2000: generate, test against the real software, find precisely where it broke, correct, and repeat, for as long as it takes. What carries over is not the format knowledge. It is the method, and the hard-won instinct for how these models fail so you can catch it.

And catching it is the whole job. The AI will confidently hand you a file that looks perfectly reasonable and is wrong in a way that changes the answer. If you cannot read LPile output and tell when a result is physically implausible, you have no business automating its input. I can, which is why I trust the tool, and why every result it helps produce still goes through the same review and the same stamp any analysis of mine would. The automation builds the file. The engineer decides whether to believe it.

## The pattern, by now

This is the third hostile format I have taught an AI to handle, after SAP2000 and the CANDE work behind my [buried-structure preprocessor](/articles/cande-editor/). At some point it stops being a series of one-off projects and becomes a capability: if your workflow is bottlenecked on some crusty legacy input format that everyone in your office dreads, there is a good chance it can be automated by someone who understands both the software and the AI well enough to do it safely. That describes a smaller group of people than you might think, and it is squarely the work I like. If it fits, the [analysis automation practice](/sap2000-ai-automation/) is the right place to start.

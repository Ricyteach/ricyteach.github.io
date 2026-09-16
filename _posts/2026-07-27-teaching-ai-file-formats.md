---
layout: article
title: "Then I Did It Again, With an Even Worse File Format"
description: "The LPile input format is unusually difficult: custom floating-point conventions, inconsistent field separators, and required typographical errors. Teaching a language model to handle it anyway."
related:
  - "sap2000-ai-tool"
  - "cande-editor"
service_page: "/sap2000-ai-automation/"
---

When I wrote about building [an artificial intelligence tool that writes SAP2000 models](/articles/sap2000-ai-tool/), the central point was that a language model is good at producing structured text but does not know any particular program's input format, and that teaching it one reliably is hard, slow work that demands deep fluency in both the software and the model. SAP2000 was simply the first program where I needed that.

## LPile, and why its input format is unusually difficult

LPile analyzes laterally loaded piles and drilled shafts. It is the standard tool for the job, and like a lot of standard engineering tools it is old, which means its text input format has accumulated decades of quirks. The SAP2000 format is unforgiving. The LPile format is worse.

A few examples, without turning this into a manual. Numbers are written in a floating-point style that standard programming libraries do not produce by default, so you cannot simply print a value and move on. The way fields are separated changes from one block of the file to the next, so a parser that works for one section corrupts another without any warning. And in a couple of places the file has to contain the program's own spelling mistakes, exactly, because the software expects them and rejects the corrected version. To make the file valid, you have to reproduce a typographical error.

None of that is in any language model's general knowledge, and none of it is forgiving. A file that is ninety-nine percent right is a file that does not load.

## Why the second format took as much work as the first

People sometimes assume that once you have done this for one program, doing it for the next one is repetition. Every one of these formats has its own rules, conventions, and failure modes, and the only way to get a tool that produces valid files every time is to go through the same grinding loop I went through for SAP2000: generate, test against the real software, find precisely where it broke, correct, and repeat, for as long as it takes. What transfers from one format to the next is the method, along with the hard-won instinct for how these models fail so you can catch it.

And catching it is the whole job. The model will confidently produce a file that looks perfectly reasonable and is wrong in a way that changes the answer. If you cannot read LPile output and tell when a result is physically implausible, you should not be automating its input. I can, which is why I trust the tool, and why every result it helps produce still goes through the same review and the same stamp any analysis of mine would. The automation builds the file. The engineer decides whether to believe it.

## The pattern, by now

This is the third difficult format I have taught a language model to handle, after SAP2000 and the CANDE work behind my [buried-structure preprocessor](/articles/cande-editor/). At some point it stops being a series of one-off projects and becomes a capability: if your work is slowed by an old input format that everyone in your office dreads, there is a good chance it can be automated by someone who understands both the software and the model well enough to do it safely. That describes a smaller group of people than you might think, and it is the work I most want to be doing. If it fits, the [analysis automation practice](/sap2000-ai-automation/) is the right place to start.

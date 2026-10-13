---
layout: article
title: "What Makes a Tool Worth Keeping"
description: "A script that ran once and gave a correct answer is disposable. A tool worth keeping has its assumptions written down, its failure modes encoded, and a verification step built in. The test I apply before building anything."
related:
  - "ai-toolkit"
  - "legacy-calc-sheets"
service_page: "/sap2000-ai-automation/"
---

Most automation in engineering starts as a script written to finish one task on one project. The script reads a results file, reformats a table, or generates fifty variants of an input file. It runs, the answer is correct, and the project continues. Sometimes that script gets saved and reused on later projects until people rely on it without anyone deciding that it had become a tool.

This article is about the difference between the script and the tool, and the test I apply before building anything.

## A script that worked once

A script written for one project encodes the conditions of that project without stating them. It assumes the units the analysis used, the naming convention of that model, the version of the program that wrote the output, and the order of the columns in a results file. On the project it was written for, every one of those assumptions was true, and the script gave a correct answer.

On the next project, some of them are false. The script usually still runs. It reads the wrong column, or converts units that were already converted, and produces a table of numbers that look reasonable. A script that fails with an error message is much less dangerous. A script that produces a wrong answer quietly is a hazard, and a script reused outside the project it was written for is a common source of that kind of wrong answer.

That kind of script is useful and disposable. The right thing to do with it after the project is to keep it as a record of what was done and decline to rely on it again without rebuilding it.

## What a tool has that a script lacks

A tool worth keeping has three things.

Its assumptions are written down. The units it expects, the program versions it has been checked against, the range of inputs it is valid for, and the conditions under which it refuses to run are stated in the tool itself, where a person reading it or using it will see them. In [The Calculation Sheet Nobody Wants to Change](/articles/legacy-calc-sheets/), I described establishing the valid range of an old calculation sheet by running it across its inputs. A tool should state that range from the start, and refuse inputs outside it.

Its failure modes are encoded. Every program and file format has traps that an experienced user knows and a new user discovers through a wrong result. The plane frame program I use, EngiLab Frame.2D, writes a text input file in which a name line may legitimately be empty, and an empty name line looks the same as a section separator. A hand edit that misreads one shifts every field after it into the wrong place. A tool can be built to handle it every time, including on the day I am fatigued. A trap that is found can be written into the tool, and the tool stops depending on my memory.

It has a verification step built in. A tool that produces analysis results also produces the evidence that those results are consistent: the sum of the reactions compared with the sum of the applied loads, a value read back from the program's own display compared with the value extracted from its output file, a result compared with a hand calculation at one point in the range. When the check fails, the tool says so plainly and stops. The check gives me something specific to examine when I review the results.

## The test before building anything

Before I build anything meant to last, I answer three questions.

The first question is how many times the tool will run. A task done once is usually faster by hand, and building a tool for it costs more than it saves. A task that repeats on every job of a certain type, or a study that needs hundreds of runs, can repay the effort of documenting assumptions and building checks. The answer has to be an honest estimate. It is easy to overestimate how often a task will recur.

The second question is what happens when the tool is wrong. A tool that formats a table for my own reference can be wrong without much consequence, because I will notice. A tool that generates the input for a structural analysis, or the numbers in a report that I sign, can produce a consequence that reaches a structure and the people who use it. The more serious the consequence, the more verification the tool needs before it is worth using at all, and some tasks would need so much verification that doing them by hand is safer.

The third question is who besides me needs to trust the output. If the only reader of the result is me, my own checking may be enough. If the result goes to a client, a plan reviewer, or another engineer, the tool has to produce output that they can check without knowing how the tool works. That usually means the tool writes its inputs, its assumptions, and its checks into what it produces, so the reader sees the same evidence I do.

## What fails the test

Some ideas fail the test on the first question. A task that seemed repetitive turns out to differ every time in ways that require judgment, so a tool would need as much attention per use as doing the work directly.

Some fail on the second question. A program whose output cannot be read reliably, or whose results cannot be checked independently, produces results I would have to verify completely by other means, which removes the reason for the tool.

Some fail during building. A tool can work on the examples it was written against and then break on the first real job, because the real input contains a case nobody anticipated. When that happens repeatedly, the honest conclusion is that the problem has more variety than the tool can cover, and the work goes back to being done by hand with the program's own interface.

The tools described in [Beyond SAP2000: Building an AI Toolkit Across the Whole Deliverable](/articles/ai-toolkit/) and the articles after it are the ones that passed. I direct each one, each tool's results are checked before they are used, and I remain professionally responsible for every deliverable that uses them, which is why the verification step is part of every tool I keep. Building and maintaining those tools is part of my [analysis automation practice](/sap2000-ai-automation/).

---
layout: article
title: "When the Software Has No Scripting Interface"
description: "Generating a valid input file is only half the problem. Most standard engineering programs cannot be driven from a script, and the numbers you need exist only in a printed report."
related:
  - "teaching-ai-file-formats"
  - "sap2000-ai-tool"
service_page: "/sap2000-ai-automation/"
---

The earlier articles in this series about [SAP2000](/articles/sap2000-ai-tool/) and [LPile](/articles/teaching-ai-file-formats/) were both about the same problem: producing an input file that the program will accept and that means what the engineer intended. Solving that problem gets you a file. It does not get you an answer. To get an answer, something has to run the program, wait for it to finish, and read the results back out.

That sounds like the easy part. It is usually the harder one.

## Why these programs cannot be scripted

Most of the standard software in structural and geotechnical engineering was written for one person sitting at one keyboard, analyzing one model at a time. That is a perfectly reasonable thing to build, and for decades it was the only thing anyone needed. What it means in practice is that these programs have no application programming interface, no scripting language, and no command line option that says solve this file and then stop.

A few of the large commercial packages do offer a programming interface, and when one exists I use it. Most of what I run does not have one. For those, automation means driving the program the way a person would, which introduces a category of problem that has nothing to do with engineering.

## The obstacles, specifically

Some of these are genuinely strange, and none of them are documented anywhere you would think to look.

One analysis program I use will not exit on its own. It finishes the run, writes its output, and then sits there. A naive loop that starts the program and waits for it to finish will complete exactly one file and then wait forever. Until you know that, the automation looks like it works on a single test case and then hangs the first time you give it real work.

Several programs open a dialog box partway through, asking a question that a human would answer without noticing. With no human present, the dialog waits indefinitely, and so does everything downstream of it. Handling that means watching for windows to appear and responding to them, which is a different discipline from anything in the analysis itself.

One program takes the base name of a file rather than the file name. Passing the full name with its extension produces a failure that does not clearly say what went wrong. Another refuses to start at all while an interactive session of the same program is open, because its automation server allows only one instance, so the automation has to check for that condition and report it clearly rather than failing in a confusing way. Another opens a file dialog during the run that, answered carelessly, can rename the project file you were trying to analyze.

Then there is the output. Several of these programs write a structured results file that contains a great deal of information and omits the specific numbers an engineer actually needs. The design criteria checks, the ones that say whether the section passes, exist only in the printed text report meant for a human reader. Getting those values means parsing a report that was formatted for a page, with headers, page breaks, and column alignment that shifts depending on the magnitude of the numbers.

## What the automation actually consists of

For each program, the working automation is a short list of unglamorous facts: how to launch it without a window taking over the screen, how to tell that the run is genuinely finished rather than merely quiet, which dialogs appear and what to do with them, how to close it cleanly so the next run starts from a known state, and where in the printed report each number lives.

None of that is engineering. All of it has to be exactly right, because a run that silently fails halfway and leaves a stale output file on disk will hand you last week's answer with this week's file name. That specific failure is the one I check for hardest. Every value the automation extracts gets verified against what the program displays on screen for at least one case in every batch, which is the only way I am willing to trust a number that no human read directly.

## What it is worth

The reason to do any of this is that it changes what questions you can afford to ask. When running a model costs ten minutes of your attention, you run the model once, with your best estimate of the inputs, and you design to that answer. When running a model costs nothing but time on a machine overnight, you run fifty of them, and you find out how sensitive your answer is to the assumption you were least sure about.

That is a different kind of engineering. It is the difference between knowing that a design works and knowing how close it came to not working, which is the more useful thing to know and the harder thing to obtain. A parametric study that would have taken a week of clicking becomes something I set running before dinner.

The tools stay fragile in one specific way, and I will not pretend otherwise. Automation that drives an interface depends on that interface staying put, so a vendor update can break it, and every one of these has broken at least once. Rebuilding it is a few hours of annoyance rather than a crisis, and the alternative is doing the clicking by hand forever.

If your work involves running the same analysis many times with different numbers, that is the situation this addresses, and it is a large part of my [analysis automation practice](/sap2000-ai-automation/).

---
layout: article
title: "I Built a CANDE Preprocessor with an AI, Before That Was Easy"
description: "The story of building a CANDE mesh editor with AI in early 2025, when there was no agent that would read your repo and build a feature, and what it took to get it right."
---

In a [previous article](/articles/what-is-cande/) I explained what CANDE is and why buried structures need soil-structure interaction analysis. Here is the part I left for later: the tool I built to make the tedious half of that work bearable.

## The chore

Preparing a CANDE model means more than drawing a mesh. Every element has to carry a material number and a construction step number, because the program builds the soil up in stages and each region behaves differently. On a real model that is hundreds of elements, and reassigning their materials and steps by hand, in a text file, is exactly as slow and error-prone as it sounds. Then there are interface elements, the special elements that let the structure slip against the soil at their boundary, with a friction value and an orientation that has to be worked out from the geometry. Building those by hand is worse.

I wanted to click and drag instead. Select a band of elements, set their material, done. Draw a box around the structure, create interfaces along it, done. So I built it.

## In 2025, this was not a casual undertaking

I want to be honest about the timeline, because it matters. I started this in early 2025, when AI coding tools were nowhere near as capable as they are now. There was no agent that would read your repo and build a feature. There was a chat window, and there was me, and there was a CANDE file format that the model did not understand and a desktop GUI it could not test.

The first working version came together as a single Python file that I iterated through roughly twenty-six rounds before I was willing to call any of them Version 1. Every round was the same loop: describe exactly what I needed, get code, run it, watch it fail or do something slightly wrong, describe the failure precisely, and go again. Later I had it restructured into a proper model-view-controller layout so it could actually grow, and that is when the interface-element and friction features went in.

The thing that made it possible was not that the AI is a good programmer. It is that I knew exactly what the tool needed to do, down to how CANDE expects the mesh oriented and how its color palette maps to materials, and I could tell immediately when the output was wrong. The AI supplied the code. I supplied the specification and the judgment about whether it was right. That division is the same one I rely on in every tool I have built since.

## What it does now

It opens a CANDE input file and draws the mesh the way CANDE thinks about it, with the vertical axis pointing up. You select elements by clicking, by dragging a box, or by filtering on material or step, with the same left-to-right versus right-to-left box behavior that anyone who uses CAD already has in their fingers. Selected elements get a marching-ants outline that stays visible against every color in the palette. You reassign materials and steps to a whole selection at once. You select the beam elements along the structure, give a friction value, and it generates the interface elements and works out their orientation for you. Then you save, and it writes the file back out without disturbing the formatting of everything you did not touch.

## Why I am telling you this

Two reasons. First, if you have buried-structure work, you are hiring someone who cares enough about getting CANDE right to have built his own tools around it. Second, this was the start of a habit. The same approach, an engineer directing an AI to build exactly the tool he needs and verifying every output, is how I later took on much harder formats and much bigger problems, including [a tool that builds full SAP2000 models from a plain-language description](/articles/sap2000-ai-tool/).

---
layout: article
title: "Editing a Drawing You Did Not Draw"
description: "Changing a drawing that somebody else produced means operating AutoCAD itself through its automation interface. What that involves, how it differs from generating a drawing, and the rule that the original file is never modified in place."
related:
  - "drawings-from-code"
  - "running-legacy-software"
service_page: "/structural-engineering/"
---

[Drawings Written in Python](/articles/drawings-from-code/) described producing drawings from code, where the geometry, layers, dimensions, and sheets all come from a program I wrote. That approach assumes I own the drawing from its first line. Drawings Written in Python also listed existing conditions and renovations among the work that generation does not suit.

Often the drawing already exists. Another designer produced it, it arrived as an AutoCAD file, and the task is to change part of it: move the existing construction to its own layers so it plots lighter than the new work, add callouts to a detail, repair a table, and plot the sheets. For that work, I drive AutoCAD itself.

## A different technical problem

Generating a drawing means writing a file in a known format. The program that writes the file controls everything in it, and the drafting application only reads the result.

Editing an existing drawing starts from a file full of things my code did not create: the other designer's layers, blocks, text styles, dimension styles, table styles, and plot settings. The dependable way to change part of that file while leaving everything else as it was is to have AutoCAD make the change, since the file format is AutoCAD's own. The work therefore consists of operating a running AutoCAD session from a script. I do that from PowerShell, through the automation interface that AutoCAD provides so that other programs can control it.

That makes it a version of the problem described in [When the Software Has No Scripting Interface](/articles/running-legacy-software/), with one difference. AutoCAD does have an automation interface, so commands can be sent through it directly. The rest of that article still applies. The application has a state, it can be busy, it can open a dialog box that waits for an answer, and the script has to confirm that each step finished before it starts the next one.

## What the work consists of

Bulk layer reassignment is the first task. A received drawing may put existing and new construction on the same layers, or use a layer scheme that differs from the standard the rest of the set follows. Selecting every object that meets a set of criteria and moving it to the correct layer is fast for a script and slow and error prone by hand. It also establishes the lineweight hierarchy, in which existing work plots lighter than new work, so that a reader of the sheet can tell the two apart.

Annotation is the second task. Multileaders, the callouts with a leader line pointing to an element, are placed with their text and leader endpoints specified, using the drawing's own multileader style so they match the annotation already on the sheet. Hatching a wall or a slab in section is the same kind of task.

Table grid visibility is a small item. As Drawings Written in Python described, a table can contain all of its data and show none of its grid lines, because the table style controls the visibility of the lines separately from the content. Correcting it means changing the style, or the overrides on the table itself, inside the drawing.

Plotting is the last step. Each layout is plotted to a Portable Document Format (PDF) file with the plot style and scale that make the lineweights appear as intended.

## The original file is never modified in place

The rule applies to every drawing received from someone else. The original file is never modified in place. Each session works on a copy, and the result is saved under a new file name.

There are three reasons. The file as received is the record of what the other party sent, and it has to remain available exactly as it arrived. A scripted edit that stops partway through, because of a dialog box, a crash, or an error in the script, leaves a partly edited drawing, and that drawing must never be confused with the original. Keeping both files also makes a comparison possible: the plot of the edited drawing can be set beside the plot of the original, and every difference between them can be accounted for.

## Checking an edit

An edit to an existing drawing can change things nobody intended to change. A selection by layer, color, or object type can include objects that met the criteria by accident, such as a note the original drafter placed on the wrong layer. A style change made to correct one table changes every table that uses that style.

The check therefore covers more than the objects meant to change. The contents of each layer are compared before and after a reassignment, every affected sheet is plotted, and those plots are read against the plots of the original. A report of success from the script is the start of that check, and nothing goes out until the plotted sheets have been read.

## Responsibility for the result

The script operates AutoCAD. I decide what changes, review every result on the plotted sheet, and remain professionally responsible for the drawings I issue. Where the drawings are signed by another licensed professional, I identify my changes and take responsibility only for the work I perform. If you have drawings from another designer that need to be revised, annotated, reorganized, or plotted as part of an engineering scope, that work is part of my [structural engineering services](/structural-engineering/).

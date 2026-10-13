---
layout: article
title: "When a Two-Dimensional Frame Model Is Enough"
description: "Many structural questions are planar, and a small plane frame program answers them with less setup and a model that is easier to check. How I build and run those models from a specification, and where a plane model stops being valid."
related:
  - "sap2000-ai-tool"
  - "running-legacy-software"
service_page: "/sap2000-ai-automation/"
---

Many structural questions are planar. A portal frame resisting wind in the direction of its rafters. A continuous beam over three or four supports. A pile bent loaded in the plane of its piles. A simple roof truss. A braced bay in the wall of a steel building. Each of these is a structure whose members, supports, and loads lie in one plane, and whose response of interest happens in that plane.

For problems of that kind, a full three-dimensional analysis package requires input that contributes nothing to the answer. The model needs a third coordinate for every node, restraints against out-of-plane movement that the real structure receives from other members, a section orientation for every member, and output for degrees of freedom that are zero by construction. Each of those is a place to make an input error, and none of them changes the forces in the members.

## When a plane model is valid

A plane frame model has three degrees of freedom at each node: two translations in the plane and one rotation about the axis perpendicular to it. It is a valid model when the members, the supports, and the loads all lie in one plane, when each member bends about a principal axis perpendicular to that plane, and when something outside the model prevents the frame from moving out of that plane. Under those conditions, a linear analysis of the same frame in three dimensions gives the same in-plane forces as the plane model. For a frame whose stability depends on its own bending stiffness, the design specification also requires second-order effects to be accounted for, either by the analysis or by amplifying the results of a first-order analysis.

The condition about out-of-plane restraint is the one to examine. In a portal frame, the girts, purlins, and wall bracing provide it. In a truss, the purlins and bracing at the panel points provide it. The plane model assumes that restraint exists, so the engineer has to confirm that it exists in the structure, and the member design still has to account for the unbraced lengths between those points.

## What a small plane frame program does well

The program I use for these models is EngiLab Frame.2D, a plane frame analysis program. A model in a program of this kind is small, which makes it fast to build, fast to run, and easy to check completely. I can look at every node and every member. The reactions can be summed against the applied loads by hand. A moment diagram for a continuous beam or a portal frame has a shape an engineer recognizes, and a diagram with the wrong shape points directly to the input that caused it.

That ease of checking is the main reason to use it. A model that can be reviewed in full is a model whose errors get found.

## Building the model from a specification

I build these models the same way I build SAP2000 models, as I described in [Why I Built an AI Tool That Writes SAP2000 Models](/articles/sap2000-ai-tool/). I write a structured description of the frame, meaning its geometry, sections, supports, and loads, and the tool writes the program's text input file from that description.

EngiLab Frame.2D has no scripting interface, no command line option to solve a file, and no results file. Running a model therefore means driving the program's own interface the way a person would and reading the results back from it, which is the class of problem described in [When the Software Has No Scripting Interface](/articles/running-legacy-software/).

The text format has a hazard of its own. A name line in the file is allowed to be empty, and an empty name line looks the same as the separator between sections of the file. A hand edit that mistakes one for the other can shift every field after it, so that each later value is read into the wrong place. A tool that writes the file has to account for this, and the model has to be checked against the specification before its results are used.

## Running a study as a batch

Once writing and running a model are automated, the useful unit of work becomes a set of related models. A span study runs the same frame at several spans to show where the governing member or the governing deflection changes. A section comparison runs the same geometry with candidate sections to show the margin each one provides. A load study varies one load to show how sensitive the result is to the value that was least certain.

Each variant is written from the same specification with one input changed, which keeps the variants consistent with each other. I review the results of every variant, and I check representative cases against a hand calculation.

## The limits

A plane frame program does not compute torsion, out-of-plane behavior, or diaphragm action. These are outside its formulation, and the error to avoid is treating a problem as planar when it involves one of them.

Torsion appears when a beam is loaded away from its shear center or supports a slab on one side only. A plane model reports no torsion in those members because it has no way to represent it.

Out-of-plane behavior includes lateral-torsional buckling of a beam and weak-axis buckling of a column. The plane analysis gives the in-plane forces. The member checks under the governing design specification then use the out-of-plane unbraced lengths, which the engineer determines from the actual bracing.

Diaphragm action is the way a roof or floor distributes lateral load among the frames below it. A building with frames of different stiffness, or with end walls much stiffer than the interior frames, shares lateral load through the diaphragm in proportions that a single frame model cannot determine. Analyzing one interior frame under its tributary wind load assumes the diaphragm redistributes nothing, and that assumption has to be justified for the building in question.

When one of these governs, the problem needs a three-dimensional model, and I build one. When none of them governs, the plane model gives the same answer with far less to check.

## Who is responsible for the answer

The tool writes files and operates the program. I decide whether the problem is planar, write the specification, review the model and every result, and remain professionally responsible for what goes out. That division applies throughout my [analysis automation work](/sap2000-ai-automation/).

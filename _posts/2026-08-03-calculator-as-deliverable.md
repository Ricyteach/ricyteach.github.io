---
layout: article
title: "Sometimes the Calculator Is the Deliverable"
description: "Some clients need a tool that designs, not a single design. What a parametric structural calculator is, why it is harder to build than a one-off analysis, and when it is the right answer."
related:
  - "ai-toolkit"
  - "sap2000-ai-tool"
service_page: "/structural-engineering/"
---

Most engineering engagements end with a stamped set of calculations for one specific project. But some of the most useful work I do does not produce a single design at all. It produces a tool that designs, that the client and their own customers use over and over without coming back to me each time.

## The idea

Picture a company that sells the same kind of structure in many variations: a carport line, a sign or scoreboard product, a racking system. Every order is a little different, different dimensions, different site, different wind and snow, different jurisdiction, but the engineering underneath is the same set of checks applied to different numbers. Paying an engineer to redo that analysis by hand for every order is slow and expensive. The better answer is to do the engineering once, thoroughly, and capture it in a calculator that produces a correct, defensible design for any valid combination of inputs.

I have built several of these. They take a configuration, the geometry, the loads, the applicable code, and return the member sizes, the connections, the foundations, the whole package, with the logic of a full structural analysis running underneath a clean front end. The client's sales or engineering staff can quote and design in minutes instead of waiting days for a one-off.

## Why it is harder than a one-off, not easier

A calculator that anyone can run is a much more demanding thing to build than a single stamped calculation, and it is worth being honest about why.

When I design one structure, I get to apply judgment at every step. A calculator has to apply that judgment automatically, for inputs I have not personally seen, which means every input has to be bounded and validated, and the tool has to refuse the cases that fall outside the envelope it was designed for rather than quietly producing a wrong answer. The hard engineering is not the arithmetic. It is defining the boundaries of where the tool is allowed to operate and making sure it stays inside them. Encoding the relevant code provisions correctly across an entire market, with different wind and snow and seismic conditions, is its own substantial effort. And it all has to be version-controlled and documented, because a calculator that silently changes its answers between revisions is a liability rather than an asset.

Done right, the calculator carries the engineering, within a clearly defined envelope, and I stand behind that envelope the same way I would behind any deliverable.

## Where the AI work pays off

This is where the tooling I have built for myself compounds. The same ability to move quickly and reliably between a design description and a verified structural model, the thing behind my [SAP2000 and broader automation work](/articles/ai-toolkit/), is exactly what makes it practical to stand up and validate a parametric calculator across an entire product line. Running the underlying analysis a hundred ways to verify the calculator agrees with first-principles models at every corner of its input space is the kind of job that used to be prohibitively tedious. It is not anymore.

If you sell a repeatable engineered product and you are paying for the same analysis again and again, a calculator might be the highest-leverage thing I can build for you. The deliverable is not a drawing. It is a tool your business keeps using. That kind of work falls squarely under my [structural engineering services](/structural-engineering/).

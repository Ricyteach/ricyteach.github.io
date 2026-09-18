---
layout: article
title: "Teaching a Program Which Loads Help and Which Hurt"
description: "Encoding load combination logic once, correctly, so every model afterward starts from the right set. The hard part is that whether a load is favorable depends on the structure, not only on the code."
related:
  - "load-combinations"
  - "sap2000-ai-tool"
service_page: "/sap2000-ai-automation/"
---

The [previous article](/articles/load-combinations/) argued that the load combination set determines whether an analysis answers the right question, and that combination errors are invisible in the output. The obvious response to an error class that is invisible, repetitive, and purely procedural is to stop performing it by hand.

That is what I have been building. It has taken longer than the model generation work did, for a reason worth explaining.

## What the easy half looks like

Most of a combination set is a direct transcription of the governing code. Given a design philosophy, a set of load cases present on the structure, and the applicable standard, the list of combinations follows from the standard with no judgment involved. Strength design combinations, allowable stress design combinations, the alternative basic set where it applies, the seismic combinations with their redundancy and overstrength variants: all of it is bookkeeping that a program does perfectly and a tired engineer does not.

The gains from encoding that part are immediate. A combination set generated from a specification is complete, which is the property a retyped set most often lacks. It is consistent between projects, so a reviewer familiar with one package can read the next one. And when the adopted code edition changes, the change happens in one place rather than in a folder of spreadsheets that each contain a slightly different vintage of the same list.

## What the hard half looks like

The difficulty is that a load combination is determined by the code together with facts about the structure that the code cannot know.

Consider the treatment of dead load. The standard says that dead load takes a reduced factor when its effect is favorable. Deciding whether it is favorable in a given combination for a given member requires knowing what that combination is checking. For the footing of a moment frame column, the dead load is favorable in the combination checking uplift on the windward column and unfavorable in the combination checking bearing on the leeward one, and those are two different combinations applied to the same load case in the same model.

The same problem appears with earth pressure, with groundwater, with superimposed dead loads that may or may not be present at the time the governing event occurs, and with any load whose sign relative to the demand depends on which failure you are checking. A tool that applies a single factor to each load case across the whole model produces a set that is correct for some members and wrong for others, which is worse than an obviously incomplete set, because it looks finished.

## How the specification solves it

The approach that works is to describe the structure's load cases in terms of their engineering role before generating anything.

Each load case is declared with the information the combination logic needs: whether it is permanent or variable, whether its presence is certain or conditional, whether it can reverse direction, and which demands it opposes rather than augments. A superimposed dead load from equipment that will definitely be installed is a different object from one that might be removed during service, even though both are dead load. Lateral earth pressure on the resisting side of a wall is a different object from earth pressure on the driving side, even though both come from the same soil.

With that declared, generating the combinations becomes mechanical again, including the favorable and unfavorable variants, and the output is a combination set where each entry knows what it is checking. The engineering happens once, at the point of declaration, in a form that can be read and reviewed by someone who was not there when it was written.

That declaration is also the part I will not let a tool guess at. It is a description of the structure, and describing the structure is the engineer's job. What the tool contributes is that the description only has to be made once, in one place, in a form precise enough to be checked.

## Connecting it to the model

The last step is translation. A combination specification is useless if turning it into a structural model still means typing a hundred rows into a dialog box, so the specification feeds directly into the [model generation work](/articles/sap2000-ai-tool/) I wrote about earlier in this series. The load cases, the patterns, and the combinations are written into the input file together, from the same source, which removes an entire class of error where the model contains a load case the combination list does not reference, or the reverse.

There is a quieter benefit to that coupling. Because the combinations and the model come from one specification, the specification is a complete statement of what was analyzed, and it goes into the calculation package as documentation. A reviewer can read what the analysis assumed without reconstructing it from the results.

## Where this currently stands

I want to be accurate about status, because I described this as in development when I [wrote about the toolkit](/articles/ai-toolkit/) earlier this year. This is a progress report. The work is not finished.

The code transcription half is working and in use. The declaration and favorability half works for the structure types I have needed it for, which means it has been exercised on real projects rather than on examples I invented for it, and it gets extended each time a structure presents a case it does not handle. That is the honest state of it. It is useful now and it is not finished, and those two things are frequently true at the same time.

If your projects involve repeated analysis under a consistent code framework, this is the layer where the errors actually live, and it is part of my [analysis automation practice](/sap2000-ai-automation/).

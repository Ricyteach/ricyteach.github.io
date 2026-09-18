# Taut Engineering article series manifest

Publication order, slugs, dates, and link plan for the tautengr.com article series. Read `CLAUDE.md` in the repository root first. Every language rule in that file applies to every article in this manifest.

The series publishes weekly on Mondays. Articles 1 through 14 are the first series, running from June 29 to September 28, 2026. Articles 15 through 29 are the second series, running from October 5, 2026 to January 11, 2027. The third series follows, beginning January 18, 2027. Its dates in the table below predate the two week shift and need renumbering before any of it is written.

Verify the published state against `_posts` before writing anything. This manifest records the plan, and the repository records what actually happened.

Run `python3 docs/check-articles.py` from the repository root before finishing any article work. It verifies the mechanical rules and prints the two categories separately: findings are failures, notes are items for a person to judge.

## Series one: published

| Number | Title | Slug | Date |
|---|---|---|---|
| 1 | Why I Built an AI Tool That Writes SAP2000 Models | /articles/sap2000-ai-tool/ | Jun 29, 2026 |
| 2 | Beyond SAP2000: Building an AI Toolkit Across the Whole Deliverable | /articles/ai-toolkit/ | Jul 6, 2026 |
| 3 | What CANDE Is, and When You Actually Need It | /articles/what-is-cande/ | Jul 13, 2026 |
| 4 | I Built a CANDE Preprocessor with an AI, Before That Was Easy | /articles/cande-editor/ | Jul 20, 2026 |
| 5 | Then I Did It Again, With an Even Worse File Format | /articles/teaching-ai-file-formats/ | Jul 27, 2026 |
| 6 | Sometimes the Calculator Is the Deliverable | /articles/calculator-as-deliverable/ | Aug 3, 2026 |
| 7 | Using AI to Check an Engineer's Work | /articles/ai-checking-work/ | Aug 10, 2026 |
| 8 | Where Is the Neutral Axis, Really? | /articles/where-is-the-neutral-axis/ | Aug 17, 2026 |
| 9 | The Buckling Mode Hot-Rolled Intuition Misses | /articles/distortional-buckling-dsm/ | Aug 24, 2026 |
| 10 | Cold-Formed Steel Is Not Just Thin Hot-Rolled Steel | /articles/cold-formed-steel/ | Aug 31, 2026 |
| 11 | How a Pile Resists a Sideways Shove | /articles/laterally-loaded-piles/ | Sep 7, 2026 |
| 12 | When the Dirt Is Not Good Enough | /articles/ground-improvement/ | Sep 14, 2026 |
| 13 | When Do You Actually Need PLAXIS? | /articles/when-you-need-plaxis/ | Sep 21, 2026 |
| 14 | Why I Take the Jobs Big Firms Turn Down | /articles/small-projects/ | Sep 28, 2026 |

The title of article 7 originally ended with a contrast pair. It was changed during the language rule editing pass. The slug is unchanged.

All fourteen were edited in September 2026 to comply with the language rules in `CLAUDE.md`. They run shorter than the 700 to 1100 word target, between roughly 510 and 850 words. Lengthening them is optional and has not been done.

## Series two: written and scheduled

All fifteen are written and in `_posts` with the dates below. Jekyll is configured with `future: false`, so each becomes visible on its date, brought online by the scheduled rebuild workflow in `.github/workflows/rebuild.yml`.

Two articles were added to the front of this series in September 2026 and the original thirteen were shifted back two weeks. The two additions are the only subjects on the site with direct evidence of search demand, since both of the projects the owner identified as having found him through a search were of those types. Their relative order within the series is unchanged, so every internal link remains backward only.

The alternation between engineering and tooling subjects is broken once, at the start, where the two additions run back to back. That was accepted deliberately. Interleaving them would have separated the companion pairs, such as the anchorage article and the article on automating anchor checks, and a forward link would have resulted.

| Number | Title | Slug | Date | Side |
|---|---|---|---|---|
| 15 | What a Shop Drawing Review Actually Checks | /articles/shop-drawing-review/ | Oct 5, 2026 | Engineering |
| 16 | Reading an Existing Structure Before You Analyze It | /articles/condition-assessment/ | Oct 12, 2026 | Engineering |
| 17 | When the Software Has No Scripting Interface | /articles/running-legacy-software/ | Oct 19, 2026 | Tooling |
| 18 | Why Anchors Fail, and Which Failure Decides the Design | /articles/concrete-anchorage-failure-modes/ | Oct 26, 2026 | Engineering |
| 19 | A Hundred Anchor Configurations Instead of One | /articles/automating-anchor-checks/ | Nov 2, 2026 | Tooling |
| 20 | The Load Combination Is the Design | /articles/load-combinations/ | Nov 9, 2026 | Engineering |
| 21 | Teaching a Program Which Loads Help and Which Hurt | /articles/automating-load-combinations/ | Nov 16, 2026 | Tooling |
| 22 | Piles Get Weaker When You Put Them Close Together | /articles/pile-group-effects/ | Nov 23, 2026 | Engineering |
| 23 | One Buried Structure Run Tells You Almost Nothing | /articles/cande-parametric-sweeps/ | Nov 30, 2026 | Tooling |
| 24 | Does This Abutment Actually Need Seismic Detailing? | /articles/abutment-seismic-design/ | Dec 7, 2026 | Engineering |
| 25 | Drawings Written in Python | /articles/drawings-from-code/ | Dec 14, 2026 | Tooling |
| 26 | What a Calculation Package Is For | /articles/calculation-package/ | Dec 21, 2026 | Engineering |
| 27 | The Calculation Sheet Nobody Wants to Change | /articles/legacy-calc-sheets/ | Dec 28, 2026 | Tooling |
| 28 | What I Look For When I Review Somebody Else's Design | /articles/how-peer-review-works/ | Jan 4, 2027 | Engineering |
| 29 | Where I Stop Automating | /articles/where-automation-stops/ | Jan 11, 2027 | Tooling |

Two working titles were improved while keeping their manifest slugs. Article 17 was "When the Software Has No API", which used an unexpanded initialism. Article 27 was "The Calculation Sheet Nobody Wants to Touch", which used a non-literal sense of a prohibited word.

The two September additions were originally numbered 34 and 38 in the third series. Their briefs have been removed from that series, and the third series now begins on January 18, 2027, after the second series ends on January 11.

## Series three: to be written

The third series continues the alternation between engineering subjects and tooling subjects. The subjects are drawn from two sources: the categories of work that appear most often in the practice, and the analysis tooling built for that work.

One deliberate correction is built into this series. The site has five service pages, and through article 27 the solar racking page has no supporting article at all, while the structural engineering page has eight. Articles 28, 29, and 32 address that gap.

| Number | Working title | Slug | Date | Side | Service page |
|---|---|---|---|---|---|
| 28 | Wind on Structures That Are Mostly Air | /articles/wind-open-structures/ | Jan 4, 2027 | Engineering | /solar-racking/ |
| 29 | One Calculator for an Entire Product Line | /articles/product-line-calculator/ | Jan 11, 2027 | Tooling | /solar-racking/ |
| 30 | Helical Piles and the Torque Correlation | /articles/helical-piles/ | Jan 18, 2027 | Engineering | /geotechnical-fea/ |
| 31 | When a Two-Dimensional Frame Model Is Enough | /articles/two-dimensional-frame-models/ | Jan 25, 2027 | Tooling | /sap2000-ai-automation/ |
| 32 | Ballast, Uplift, and the Roof Underneath | /articles/ballasted-rooftop-arrays/ | Feb 1, 2027 | Engineering | /solar-racking/ |
| 33 | The Signature Curve | /articles/signature-curve/ | Feb 8, 2027 | Tooling | /structural-engineering/ |
| 35 | Editing a Drawing You Did Not Draw | /articles/editing-existing-drawings/ | Feb 22, 2027 | Tooling | /structural-engineering/ |
| 36 | Removing a Wall | /articles/removing-a-wall/ | Mar 1, 2027 | Engineering | /structural-engineering/ |
| 37 | Assembling the Report Without Retyping the Numbers | /articles/report-assembly/ | Mar 8, 2027 | Tooling | /sap2000-ai-automation/ |
| 39 | What Makes a Tool Worth Keeping | /articles/what-makes-a-tool-worth-keeping/ | Mar 22, 2027 | Tooling | /sap2000-ai-automation/ |
| 40 | Peer Review and Independent Engineering Review | /articles/independent-engineering-review/ | Mar 29, 2027 | Engineering | /structural-engineering/ |

## Series three briefs

### 28. Wind on Structures That Are Mostly Air

Carports, canopies, shade structures, sports netting, freestanding signs, and ground-mount racking are all open structures, and the wind provisions that apply to them are not the enclosed building provisions most engineers use daily. Explain the distinction between an enclosed building, a partially enclosed building, an open building, and the other structures category, and why applying enclosed building pressure coefficients to an open frame produces the wrong answer in both directions depending on the case. Cover net pressure acting on both faces of an open element, the way effective wind area changes the coefficient, and why uplift usually governs on a light structure where the dead load is small. Do not reproduce specific coefficient values. Point at the governing standard and edition.

Internal links: /articles/load-combinations/. Service page: /solar-racking/.

### 29. One Calculator for an Entire Product Line

Companion to article 28 and an extension of article 6. A company selling carports, racking, or netting across many jurisdictions needs a design for every order, and the input space is the site conditions multiplied by the configuration options. Describe what has to be bounded: wind speed, exposure category, snow, seismic parameters, and the geometric options, along with the code edition, which varies by jurisdiction and is an input rather than a constant. Explain validating the calculator at the corners of the input space rather than in the middle, and refusing inputs outside the envelope. Reference the anchor sweep article as the same idea at smaller scale.

Internal links: /articles/calculator-as-deliverable/, /articles/wind-open-structures/. Service page: /solar-racking/.

### 30. Helical Piles and the Torque Correlation

Helical piles resist load through bearing on the helix plates rather than primarily through shaft friction, which makes them suitable for tension and uplift as well as compression. Explain where they fit: limited access sites, retrofit and underpinning, light structures, and situations where installation must produce no spoil and no cure time. Cover the torque correlation honestly, meaning that installation torque correlates with capacity through an empirical factor that depends on the shaft, and that this gives a verification during installation which most foundation types do not have, while remaining a correlation rather than a measurement. Cover the limits: lateral capacity is modest because the shaft is slender, and the design is sensitive to whether the helices reach competent bearing material.

Internal links: /articles/laterally-loaded-piles/, /articles/pile-group-effects/. Service page: /geotechnical-fea/.

### 31. When a Two-Dimensional Frame Model Is Enough

A large fraction of real structural questions are planar: a portal frame, a continuous beam, a pile bent, a simple truss, a braced bay. Argue that reaching for a full three-dimensional package for these costs setup time and adds nothing, and describe what a small plane frame program does well. Cover building the model from a specification rather than through an interface, running a span study or a section comparison as a batch, and the honest limits, which are that torsion, out-of-plane behavior, and diaphragm action are not available and pretending otherwise is the failure mode.

Internal links: /articles/sap2000-ai-tool/, /articles/running-legacy-software/. Service page: /sap2000-ai-automation/.

### 32. Ballast, Uplift, and the Roof Underneath

A ballasted rooftop array resists wind uplift and sliding with weight rather than with roof penetrations, which turns the design into a minimum dead load problem and connects directly to article 18. Cover the three questions: does the array stay in place, does the roof structure accept the concentrated ballast loads, and does the roof assembly itself tolerate the array. Explain the difference between manufacturer wind tunnel data and code pressure coefficients, and what it means to apply wind tunnel data to a specific site. Cover roof zones, where corner and edge zones see substantially higher pressure and therefore more ballast, and the practical consequence that a uniform ballast layout is either unsafe at the corners or wasteful in the field.

Internal links: /articles/wind-open-structures/, /articles/load-combinations/. Service page: /solar-racking/.

### 33. The Signature Curve

The finite strip elastic buckling analysis behind article 9, treated on its own. Explain what the curve plots, which is buckling load factor against half-wavelength, and how to read it: the local minimum at short wavelength, the distortional minimum at intermediate wavelength, and the descending branch at long wavelength that represents global buckling. Explain what changes the curve, including lip length, intermediate stiffeners, and thickness, so the reader can see why cold-formed sections are shaped the way they are. Explain what the curve does not tell you, which is strength, since it gives elastic buckling loads that then feed the strength equations.

Internal links: /articles/distortional-buckling-dsm/, /articles/cold-formed-steel/. Service page: /structural-engineering/.


### 35. Editing a Drawing You Did Not Draw

Companion to article 23, covering the opposite situation. Generating a drawing from code assumes you own the drawing. Frequently the drawing already exists, it came from somebody else, and the task is to change part of it. Describe driving the drafting application itself: bulk layer reassignment, adding annotation, controlling table grid visibility, and plotting to a sheet. Explain why this is a different technical problem from generating a file, since it means operating a running application rather than writing bytes, and connect that to article 15. Include the practical rule that the original file is never modified in place.

Internal links: /articles/drawings-from-code/, /articles/running-legacy-software/. Service page: /structural-engineering/.

### 36. Removing a Wall

The most common residential question, written for homeowners and contractors. How to determine whether a wall is load bearing, which is not settled by whether it feels solid. What the load path above it is, where the new beam has to deliver its reactions, and why the posts below the beam frequently need a footing that does not exist yet. Cover deflection limits governed by finishes rather than by strength, temporary shoring during the work, and why the answer sometimes involves the foundation. Keep it specific and practical. This is the article most likely to reach people who have never hired an engineer.

Internal links: /articles/small-projects/. Service page: /structural-engineering/.

### 37. Assembling the Report Without Retyping the Numbers

Companion to article 24. The calculation package is the deliverable, and assembling it is where numbers get transcribed between applications, which is an error class rather than an inconvenience. Describe template driven assembly: the project record holds the identifying information once, the analysis results are read from where they were produced rather than retyped, and the formatting is applied consistently. Cover the parts that stay manual, which are the narrative, the assumptions, and the limitations. Explain why this was worth building even though nothing in it is technically interesting.

Internal links: /articles/calculation-package/, /articles/ai-toolkit/. Service page: /sap2000-ai-automation/.


### 39. What Makes a Tool Worth Keeping

The distinction between a script written for one project and a capability that survives. A script that ran once and produced a correct answer is disposable. A tool worth keeping has its assumptions written down, its failure modes encoded rather than remembered, and a verification step built into it. Describe the test applied before building anything: how many times will this run, what happens when it is wrong, and who besides me needs to trust the output. Be honest that several tools failed that test and were abandoned. This is the closing statement on the tooling side of the practice.

Internal links: /articles/where-automation-stops/, /articles/ai-toolkit/. Service page: /sap2000-ai-automation/.

### 40. Peer Review and Independent Engineering Review

Two engagements that get conflated. A peer review examines another engineer's design for technical adequacy, usually for the owner or for the designer of record. An independent engineering review, commissioned by a lender or an investor, asks a different question, which is whether the project as designed presents acceptable technical risk to the party financing it. Cover the differences in scope, deliverable, and independence requirements, and explain what each one does not cover. This article supports work in both the structural and the solar racking areas of the practice.

Internal links: /articles/how-peer-review-works/, /articles/calculation-package/. Service page: /structural-engineering/.

## Retroactive link edits

Internal links point backward in time only, so a few useful connections can only be added after their target publishes. Make each edit in its own small pull request on or after the date shown.

| Make on or after | Edit |
|---|---|
| Oct 12, 2026 | In `/articles/cold-formed-steel/`, the paragraph about connections in thin material gains a link to `/articles/concrete-anchorage-failure-modes/`. |
| Nov 9, 2026 | In `/articles/laterally-loaded-piles/`, the sentence about pile groups and p-multipliers gains a link to `/articles/pile-group-effects/`. |
| Nov 16, 2026 | In `/articles/what-is-cande/`, the closing note about the preprocessor gains a second link to `/articles/cande-parametric-sweeps/`. |
| Dec 7, 2026 | In `/articles/ai-checking-work/`, the paragraph about consistency checking gains a link to `/articles/calculation-package/`. |
| Jan 18, 2027 | In `/articles/pile-group-effects/`, the discussion of when a single pile analysis is adequate gains a link to `/articles/helical-piles/`. |
| Feb 8, 2027 | In `/articles/distortional-buckling-dsm/`, the paragraph about finite strip analysis gains a link to `/articles/signature-curve/`. |
| Feb 22, 2027 | In `/articles/drawings-from-code/`, the section on what this does not suit gains a link to `/articles/editing-existing-drawings/`. |

## Known exceptions

`/articles/what-is-cande/`, published June 2026, closes with a link to `/articles/cande-editor/`, which published one week later. That link returned a 404 for its first week. Both articles are now published and the link resolves, so it has been left in place. The checking script reports it as a note rather than a finding. Do not repeat the pattern.

## Planning notes

Keep the alternation between engineering subjects and tooling subjects. If an article gets cut or replaced, replace it with one from the same side of the alternation so the pattern holds.

Watch the service page balance. Through article 40 the distribution is roughly eleven articles for structural engineering, seven for analysis automation, four for geotechnical work, three for solar racking, and three for buried structures. Solar racking and buried structures are the pages that would benefit most from further coverage.

Subjects considered and not yet scheduled, available if a replacement is needed:

- Foundations for tanks and other structures that are mostly liquid, covering ring walls, slabs on grade for irrigation and water tanks, differential settlement across a large diameter, and why the contents govern.
- Structural notation, and why a detail either reads clearly to a fabricator or does not.
- Scour at pile and shaft foundations, and how a scour condition changes a lateral analysis.
- Elevated equipment platforms and industrial access structures, including vibration and serviceability.
- What a good engineering scope actually defines, written from the proposal side.
- Pole barn and post frame construction, which arrives regularly and is poorly served by general residential guidance.

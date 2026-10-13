# Taut Engineering article series manifest

Publication order, slugs, dates, and link plan for the tautengr.com article series. Read `CLAUDE.md` in the repository root first. Every language rule in that file applies to every article in this manifest.

The series publishes weekly on Mondays. Verify the published state against `_posts` before writing anything. This manifest records the plan, and the repository records what actually happened.

Run `python3 docs/check-articles.py` from the repository root before finishing any article work. It verifies the mechanical rules and prints the two categories separately: findings are failures, notes are items for a person to judge.

## Release strategy (revised October 13, 2026)

The schedule from October 19, 2026 onward was rebuilt in October 2026 after a review of the practice's actual work. The earlier plan alternated strictly between engineering subjects and tooling subjects. The revised plan rotates between three audiences instead.

1. **Property owners, buyers, real estate agents, investors, and contractors.** Recent direct inquiries, several of them through the website, have come from owners, buyers, agents, and investors in the Dayton, Springfield, and Columbus areas with a problem in an existing building: deteriorated crawlspace framing in a rental, cracked brick and block before a sale, a bowing basement wall found by a buyer's home inspection, fire-damaged framing under a city enforcement order, and a water-damaged bearing wall the city required an engineer to evaluate. The Upwork history adds a long run of residential framing work for contractors and homeowners: beam sizing, wall removal, porch and roof framing, post frame buildings, and footings. These articles are written for a reader who has never hired an engineer, and they answer the question that reader would type into a search engine.
2. **Fabricators and companies that sell engineered products or specialty structures.** Repeat work in this group includes sports netting pole and foundation reviews, sign foundations, carport and racking calculators, equipment pads with concrete anchorage, tanks, and rooftop solar permit letters. These clients return, and some become larger engagements.
3. **Engineers and technical buyers, including the tooling articles.** These establish depth and support the analysis automation service page. They remain in the schedule at roughly one week in three rather than one week in two.

Rules that follow from the strategy:

- Articles for the first audience name the region once where it reads naturally (I am based in Dayton and make site visits in the Dayton and Columbus areas), link the [condition assessment page](/condition-assessment/) or the structural engineering page, and end with what to send me. They must stay within the facts: no invented fees, no invented case histories, no client or address details.
- The first audience is concentrated in the first four months of the schedule, because search engines take weeks to months to index and rank a new page, and the residential sale season and the spring thaw both arrive in March and April.
- Companion pairs keep their order (an engineering article before the tooling article that builds on it), but they no longer run in consecutive weeks. Wording such as "the previous article" was changed to name the earlier article instead.
- Published articles were reviewed and were not re-dated. Their web addresses do not contain the date, so re-dating would only reorder the archive and the feed without any benefit, and moving a published article to a future date would remove it from the site until that date.

Articles are a modest part of local search ranking. Published local search surveys rank a dedicated page for each service, city and neighborhood relevance of that page, and the Google Business Profile primary category and address far above blog content for map results. The backlog item "Local search improvements" records the site changes that would do more for local inquiries than articles alone.

## Published

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
| 15 | What a Shop Drawing Review Actually Checks | /articles/shop-drawing-review/ | Oct 5, 2026 |
| 16 | Reading an Existing Structure Before You Analyze It | /articles/condition-assessment/ | Oct 12, 2026 |

The title of article 7 originally ended with a contrast pair. It was changed during the language rule editing pass. The slug is unchanged.

Articles 1 through 14 were edited in September 2026 to comply with the language rules in `CLAUDE.md`. They run shorter than the 700 to 1100 word target, between roughly 510 and 850 words. Lengthening them is optional and has not been done.

## Schedule

Status values: **Written** (in `_posts` with this date), **To write** (a brief exists below), **New brief** (added in the October 2026 revision, brief below).

Audience: **Owners** (property owners, buyers, agents, investors, contractors), **Specialty** (fabricators and engineered product companies), **Engineers** (engineering subjects for a technical reader), **Tooling** (analysis automation).

Jekyll is configured with `future: false`, so each written article becomes visible on its date, brought online by the scheduled rebuild workflow in `.github/workflows/rebuild.yml`.

| Number | Title | Slug | Date | Audience | Service page | Status |
|---|---|---|---|---|---|---|
| 17 | What a Bowing Basement Wall Is Telling You | /articles/bowing-basement-walls/ | Oct 19, 2026 | Owners | /condition-assessment/ | New brief |
| 18 | Why Anchors Fail, and Which Failure Decides the Design | /articles/concrete-anchorage-failure-modes/ | Oct 26, 2026 | Specialty | /structural-engineering/ | Written |
| 19 | Which Cracks in Brick and Block Walls Mean Something | /articles/masonry-cracks/ | Nov 2, 2026 | Owners | /condition-assessment/ | New brief |
| 20 | When the Software Has No Scripting Interface | /articles/running-legacy-software/ | Nov 9, 2026 | Tooling | /sap2000-ai-automation/ | Written |
| 21 | Removing a Wall | /articles/removing-a-wall/ | Nov 16, 2026 | Owners | /structural-engineering/ | To write |
| 22 | The Load Combination Is the Design | /articles/load-combinations/ | Nov 23, 2026 | Engineers | /structural-engineering/ | Written |
| 23 | Rot, Insects, and Water: Evaluating Damaged Wood Framing | /articles/damaged-wood-framing/ | Nov 30, 2026 | Owners | /condition-assessment/ | New brief |
| 24 | A Hundred Anchor Configurations Instead of One | /articles/automating-anchor-checks/ | Dec 7, 2026 | Tooling | /sap2000-ai-automation/ | Written |
| 25 | Wind on Structures That Are Mostly Air | /articles/wind-open-structures/ | Dec 14, 2026 | Specialty | /solar-racking/ | To write |
| 26 | Teaching a Program Which Loads Help and Which Hurt | /articles/automating-load-combinations/ | Dec 21, 2026 | Tooling | /sap2000-ai-automation/ | Written |
| 27 | What a Calculation Package Is For | /articles/calculation-package/ | Dec 28, 2026 | Engineers | /structural-engineering/ | Written |
| 28 | When a Report Says to Call a Structural Engineer | /articles/call-a-structural-engineer/ | Jan 4, 2027 | Owners | /condition-assessment/ | New brief |
| 29 | Drawings Written in Python | /articles/drawings-from-code/ | Jan 11, 2027 | Tooling | /structural-engineering/ | Written |
| 30 | Underpinning a House with Helical Piles | /articles/helical-piles/ | Jan 18, 2027 | Owners | /geotechnical-fea/ | To write |
| 31 | Piles Get Weaker When You Put Them Close Together | /articles/pile-group-effects/ | Jan 25, 2027 | Engineers | /geotechnical-fea/ | Written |
| 32 | Solar Panels on an Existing Roof: What the Structural Letter Checks | /articles/rooftop-solar-letter/ | Feb 1, 2027 | Specialty | /solar-racking/ | New brief |
| 33 | One Calculator for an Entire Product Line | /articles/product-line-calculator/ | Feb 8, 2027 | Tooling | /solar-racking/ | To write |
| 34 | After a Fire: Evaluating Fire-Damaged Framing | /articles/fire-damaged-framing/ | Feb 15, 2027 | Owners | /condition-assessment/ | New brief |
| 35 | The Calculation Sheet Nobody Wants to Change | /articles/legacy-calc-sheets/ | Feb 22, 2027 | Tooling | /sap2000-ai-automation/ | Written |
| 36 | What I Look For When I Review Somebody Else's Design | /articles/how-peer-review-works/ | Mar 1, 2027 | Engineers | /structural-engineering/ | Written |
| 37 | Post Frame Buildings Are Engineered Differently | /articles/post-frame-buildings/ | Mar 8, 2027 | Owners | /structural-engineering/ | New brief |
| 38 | One Buried Structure Run Tells You Almost Nothing | /articles/cande-parametric-sweeps/ | Mar 15, 2027 | Tooling | /cande-buried-structures/ | Written |
| 39 | Tall Poles and Light Nets: Sports Netting Structures | /articles/sports-netting-structures/ | Mar 22, 2027 | Specialty | /shop-drawing-review/ | New brief |
| 40 | Does This Abutment Actually Need Seismic Detailing? | /articles/abutment-seismic-design/ | Mar 29, 2027 | Engineers | /geotechnical-fea/ | Written |
| 41 | Ballast, Uplift, and the Roof Underneath | /articles/ballasted-rooftop-arrays/ | Apr 5, 2027 | Specialty | /solar-racking/ | To write |
| 42 | When a Two-Dimensional Frame Model Is Enough | /articles/two-dimensional-frame-models/ | Apr 12, 2027 | Tooling | /sap2000-ai-automation/ | To write |
| 43 | Foundations for Tanks | /articles/tank-foundations/ | Apr 19, 2027 | Specialty | /structural-engineering/ | New brief |
| 44 | The Signature Curve | /articles/signature-curve/ | Apr 26, 2027 | Engineers | /structural-engineering/ | To write |
| 45 | Why the Floor Slopes | /articles/sagging-floors/ | May 3, 2027 | Owners | /condition-assessment/ | New brief |
| 46 | Editing a Drawing You Did Not Draw | /articles/editing-existing-drawings/ | May 10, 2027 | Tooling | /structural-engineering/ | To write |
| 47 | Peer Review and Independent Engineering Review | /articles/independent-engineering-review/ | May 17, 2027 | Engineers | /structural-engineering/ | To write |
| 48 | Assembling the Report Without Retyping the Numbers | /articles/report-assembly/ | May 24, 2027 | Tooling | /sap2000-ai-automation/ | To write |
| 49 | What Makes a Tool Worth Keeping | /articles/what-makes-a-tool-worth-keeping/ | May 31, 2027 | Tooling | /sap2000-ai-automation/ | To write |
| 50 | Where I Stop Automating | /articles/where-automation-stops/ | Jun 7, 2027 | Tooling | /sap2000-ai-automation/ | Written |

Articles 17, 19, 21, and 23 were written in the same revision, each in its own pull request. Their status changes to Written when those pull requests merge. Merge the pull request that re-dated the written articles before any of them, or two articles will publish on October 19.

Service page balance through article 50, counting published articles: structural engineering sixteen, analysis automation eleven, condition assessment seven, geotechnical six, solar racking four, buried structures three, shop drawing review two, and one article that links only the contact form. Buried structures and shop drawing review remain the thinnest pages. Add a buried structures subject if one is needed as a replacement.

Two working titles were improved earlier while keeping their slugs. "When the Software Has No API" used an unexpanded initialism, and "The Calculation Sheet Nobody Wants to Touch" used a non-literal sense of a prohibited word.

## Briefs

Briefs are listed in schedule order. Articles marked Written have no brief, since the article itself is the record.

### 17. What a Bowing Basement Wall Is Telling You

The most common foundation question in older Ohio housing stock with concrete block basements. Explain what bowing is: the wall bending inward between its supports at the floor framing above and the slab or footing below, under lateral soil pressure. Cover the evidence: a horizontal crack near mid height or along a mortar joint, stair-step cracking toward the corners, shear displacement at the base, and how to measure inward deflection with a string line or level rather than by eye. Cover the usual causes in plain terms: saturated soil from poor drainage, frost, clay that swells, and surcharge near the wall. Explain why drainage comes first in any repair discussion, then the repair families at a general level (bracing with steel members, wall anchors into the yard, carbon fiber straps, excavation and rebuilding) and which conditions each suits, without fees or product endorsements. Explain the question a home inspection report cannot answer, which is whether the movement is ongoing, and how monitoring answers it. Written for buyers, sellers, agents, and landlords.

Internal links: /articles/condition-assessment/, /articles/small-projects/. Service page: /condition-assessment/.

### 19. Which Cracks in Brick and Block Walls Mean Something

Crack patterns in brick veneer and concrete block, written for an owner preparing to sell or a buyer reading an inspection report. Shrinkage and thermal cracks, cracks that follow mortar joints in a stair-step pattern, vertical cracks through the units, horizontal cracks, and tapered cracks that are wider at one end. What width, direction, and taper suggest about the cause, and the limits of reading a crack from a photograph. Old, stable movement versus active movement, and how a painted or patched crack that has reopened answers that. Brick veneer is usually a curtain in front of the structure rather than the structure itself, so cracked veneer and a cracked foundation are different questions. Monitoring as a way to answer the question of activity over a season. Drainage and downspout discharge as the most common practical recommendation.

Internal links: /articles/condition-assessment/, /articles/bowing-basement-walls/. Service page: /condition-assessment/.

### 21. Removing a Wall

The most common residential question, written for homeowners and contractors. How to determine whether a wall is load bearing, which is not settled by whether it feels solid. What the load path above it is, where the new beam has to deliver its reactions, and why the posts below the beam frequently need a footing that does not exist yet. Cover beam options (dimensional lumber, engineered lumber, steel, and a flush beam versus a dropped beam), deflection limits governed by finishes rather than by strength, temporary shoring during the work, and why the answer sometimes involves the foundation. Keep it specific and practical. This is the article most likely to reach people who have never hired an engineer.

Internal links: /articles/small-projects/, /articles/condition-assessment/. Service page: /structural-engineering/.

### 23. Rot, Insects, and Water: Evaluating Damaged Wood Framing

Deteriorated sill plates, rim joists, joist ends, and studs at the base of walls, written for landlords, investors, and owners. Where the damage concentrates and why (sills and rim joists near grade, below leaking gutters and downspouts, at plumbing walls). How the extent is established in the field: probing with an awl, sounding, a moisture meter, and opening finishes where needed, and why the extent is almost always larger than what is visible. Why the cause has to be identified before the repair is designed, since replacing framing without stopping the water repeats the job. Termite and other insect damage versus decay, and why a structural evaluation does not substitute for a pest inspection. Repair families at a general level: sistering, replacing sections with temporary support, and new bearing. Note that a city may require an engineer's letter before a permit for the repair.

Internal links: /articles/condition-assessment/, /articles/removing-a-wall/. Service page: /condition-assessment/.

### 25. Wind on Structures That Are Mostly Air

Carports, canopies, shade structures, sports netting, freestanding signs, and ground-mount racking are all open structures, and the wind provisions that apply to them are not the enclosed building provisions most engineers use daily. Explain the distinction between an enclosed building, a partially enclosed building, an open building, and the other structures category, and why applying enclosed building pressure coefficients to an open frame produces the wrong answer in both directions depending on the case. Cover net pressure acting on both faces of an open element, the way effective wind area changes the coefficient, solidity ratio for nets and lattice, and why uplift usually governs on a light structure where the dead load is small. Do not reproduce specific coefficient values. Point at the governing standard and edition.

Internal links: /articles/load-combinations/, /articles/laterally-loaded-piles/. Service page: /solar-racking/.

### 28. When a Report Says to Call a Structural Engineer

Written for the buyer, the seller, the agent, and the investor holding a home inspection report, an insurance adjuster's note, or a city notice that says to have a structural engineer evaluate something. Explain what that sentence means and what it does not: the inspector is a generalist who has identified a condition outside the scope of a home inspection. Explain the practical sequence: what to send the engineer first, whether a photo review can answer the question, how scope is set (one item versus every structural item in the report), what the deliverable is (a stamped findings letter), and how long it takes relative to a purchase contingency period. Explain reliance, meaning who may rely on the letter, and why a letter written for a seller can be shared with a buyer for information. Explain what happens when a city requires an engineer's evaluation before repairs or occupancy, which is common in rehabilitation of vacant properties. No fees and no case details.

Internal links: /articles/condition-assessment/, /articles/bowing-basement-walls/. Service page: /condition-assessment/.

### 30. Underpinning a House with Helical Piles

Helical piles resist load through bearing on the helix plates rather than primarily through shaft friction, which makes them suitable for tension and uplift as well as compression and for underpinning an existing foundation from beside it. Lead with the underpinning case, since that is the version of this work the practice actually does: a settling or newly loaded wall, a bracket attached to the existing footing, and piles advanced to competent bearing. Cover the torque correlation honestly, meaning that installation torque correlates with capacity through an empirical factor that depends on the shaft, and that this gives a verification during installation which most foundation types do not have, while remaining a correlation rather than a measurement. Cover the limits: lateral capacity is modest because the shaft is slender, the existing footing has to be able to span between brackets, and the design is sensitive to whether the helices reach competent bearing material.

Internal links: /articles/laterally-loaded-piles/, /articles/ground-improvement/. Service page: /geotechnical-fea/.

### 32. Solar Panels on an Existing Roof: What the Structural Letter Checks

Written for solar permit designers and installers who need a structural letter for a residential rooftop array. The questions the letter answers: whether the existing rafters or trusses accept the added dead load, what wind uplift does at the attachments and whether the attachment withdrawal capacity into the framing is adequate, how roof zones near edges and corners change the attachment spacing, and how snow interacts with panels. Explain what information makes the letter fast (rafter size, spacing, span, roof pitch, attachment product, layout) and why photographs of the attic framing settle most questions. Explain the limits of a letter based on photographs. Do not quote fees or turnaround promises beyond what is stated on the service page.

Internal links: /articles/load-combinations/, /articles/wind-open-structures/. Service page: /solar-racking/.

### 33. One Calculator for an Entire Product Line

Companion to article 25 and an extension of article 6. A company selling carports, racking, signs, or netting across many jurisdictions needs a design for every order, and the input space is the site conditions multiplied by the configuration options. Describe what has to be bounded: wind speed, exposure category, snow, seismic parameters, and the geometric options, along with the code edition, which varies by jurisdiction and is an input rather than a constant. Explain validating the calculator at the corners of the input space rather than in the middle, and refusing inputs outside the envelope. Reference the anchor sweep article as the same idea at smaller scale.

Internal links: /articles/calculator-as-deliverable/, /articles/wind-open-structures/. Service page: /solar-racking/.

### 34. After a Fire: Evaluating Fire-Damaged Framing

Written for owners and investors rehabilitating a building after a fire, often under a city order. Explain how wood behaves in a fire: the char layer, the heated zone behind it, and why a member that looks burned on the surface may retain most of its section while one that looks sound may be weakened. Explain how the evaluation proceeds: removing finishes in the affected area, measuring the residual section, checking connections and fasteners, which lose capacity in heat, and checking whether water from firefighting caused damage of its own. Explain that a structural evaluation addresses framing capacity only, and that fire separation, egress, and code compliance of the rehabilitation are architectural questions for an architect or the building department. Repair approaches at a general level.

Internal links: /articles/damaged-wood-framing/, /articles/call-a-structural-engineer/. Service page: /condition-assessment/.

### 37. Post Frame Buildings Are Engineered Differently

Pole barns, post frame garages, and post frame homes, written for owners and builders. Explain how a post frame building resists load: embedded or bracketed posts, girts and purlins, and a roof and wall diaphragm that transfers wind to the end walls. Explain why the embedded post foundation is a lateral design problem (connect to the laterally loaded piles article), why the diaphragm is usually the part residential rules of thumb get wrong, and what changes when a post frame building becomes a residence. Cover the documentation a building department typically wants.

Internal links: /articles/laterally-loaded-piles/, /articles/wind-open-structures/. Service page: /structural-engineering/.

### 39. Tall Poles and Light Nets: Sports Netting Structures

Written for netting fabricators and installers. A sports netting system is a set of tall cantilevered poles whose demand is almost entirely wind on a porous net, plus the net tension itself. Cover solidity of the net and how it enters the wind calculation, the load case with the net raised versus lowered or removed, pole design for combined bending and axial load, and the drilled pier foundation, which is a lateral load problem. Describe what a review of a fabricator's pole and pier drawing checks, connecting to the shop drawing review article. No client or facility names.

Internal links: /articles/wind-open-structures/, /articles/shop-drawing-review/. Service page: /shop-drawing-review/.

### 41. Ballast, Uplift, and the Roof Underneath

A ballasted rooftop array resists wind uplift and sliding with weight rather than with roof penetrations, which turns the design into a minimum dead load problem and connects directly to the load combination article. Cover the three questions: does the array stay in place, does the roof structure accept the concentrated ballast loads, and does the roof assembly itself tolerate the array. Explain the difference between manufacturer wind tunnel data and code pressure coefficients, and what it means to apply wind tunnel data to a specific site. Cover roof zones, where corner and edge zones see substantially higher pressure and therefore more ballast, and the practical consequence that a uniform ballast layout is either unsafe at the corners or wasteful in the field.

Internal links: /articles/rooftop-solar-letter/, /articles/load-combinations/. Service page: /solar-racking/.

### 42. When a Two-Dimensional Frame Model Is Enough

A large fraction of real structural questions are planar: a portal frame, a continuous beam, a pile bent, a simple truss, a braced bay. Argue that reaching for a full three-dimensional package for these costs setup time and adds nothing, and describe what a small plane frame program does well. Cover building the model from a specification rather than through an interface, running a span study or a section comparison as a batch, and the honest limits, which are that torsion, out-of-plane behavior, and diaphragm action are not available and pretending otherwise is the failure mode.

Internal links: /articles/sap2000-ai-tool/, /articles/running-legacy-software/. Service page: /sap2000-ai-automation/.

### 43. Foundations for Tanks

Water, irrigation, and process tanks, written for owners and tank suppliers. The contents govern: a full tank is a large, nearly uniform load over a large area, which makes settlement and differential settlement across the diameter the controlling questions rather than bearing alone. Cover ring wall foundations versus slab foundations, the edge of the slab where the shell bears, anchorage against wind and seismic overturning for an empty tank, and why the empty and full conditions govern different checks. Connect to the load combination article for the full versus empty logic.

Internal links: /articles/load-combinations/, /articles/ground-improvement/. Service page: /structural-engineering/.

### 44. The Signature Curve

The finite strip elastic buckling analysis behind article 9, treated on its own. Explain what the curve plots, which is buckling load factor against half-wavelength, and how to read it: the local minimum at short wavelength, the distortional minimum at intermediate wavelength, and the descending branch at long wavelength that represents global buckling. Explain what changes the curve, including lip length, intermediate stiffeners, and thickness, so the reader can see why cold-formed sections are shaped the way they are. Explain what the curve does not tell you, which is strength, since it gives elastic buckling loads that then feed the strength equations.

Internal links: /articles/distortional-buckling-dsm/, /articles/cold-formed-steel/. Service page: /structural-engineering/.

### 45. Why the Floor Slopes

Sloping and sagging floors in older houses, written for owners and buyers. Measure the slope rather than feel it, at enough points to tell a local sag from a whole-building tilt. Common causes in plain terms: undersized or overspanned joists, joists notched or cut for plumbing, a removed or relocated post, a beam with a failed splice, settlement of an interior pier, and long-term creep. Why jacking a floor back to level has to be slow and is sometimes the wrong goal. Repair families at a general level: sistering, a new beam and posts with footings, and correcting the cause before the symptom.

Internal links: /articles/condition-assessment/, /articles/removing-a-wall/. Service page: /condition-assessment/.

### 46. Editing a Drawing You Did Not Draw

Companion to article 29, covering the opposite situation. Generating a drawing from code assumes you own the drawing. Frequently the drawing already exists, it came from somebody else, and the task is to change part of it. Describe driving the drafting application itself: bulk layer reassignment, adding annotation, controlling table grid visibility, and plotting to a sheet. Explain why this is a different technical problem from generating a file, since it means operating a running application rather than writing bytes, and connect that to article 20. Include the practical rule that the original file is never modified in place.

Internal links: /articles/drawings-from-code/, /articles/running-legacy-software/. Service page: /structural-engineering/.

### 47. Peer Review and Independent Engineering Review

Two engagements that get conflated. A peer review examines another engineer's design for technical adequacy, usually for the owner or for the designer of record. An independent engineering review, commissioned by a lender or an investor, asks a different question, which is whether the project as designed presents acceptable technical risk to the party financing it. Cover the differences in scope, deliverable, and independence requirements, and explain what each one does not cover. This article supports work in both the structural and the solar racking areas of the practice.

Internal links: /articles/how-peer-review-works/, /articles/calculation-package/. Service page: /structural-engineering/.

### 48. Assembling the Report Without Retyping the Numbers

Companion to article 27. The calculation package is the deliverable, and assembling it is where numbers get transcribed between applications, which is an error class rather than an inconvenience. Describe template driven assembly: the project record holds the identifying information once, the analysis results are read from where they were produced rather than retyped, and the formatting is applied consistently. Cover the parts that stay manual, which are the narrative, the assumptions, and the limitations. Explain why this was worth building even though nothing in it is technically interesting.

Internal links: /articles/calculation-package/, /articles/ai-toolkit/. Service page: /sap2000-ai-automation/.

### 49. What Makes a Tool Worth Keeping

The distinction between a script written for one project and a capability that survives. A script that ran once and produced a correct answer is disposable. A tool worth keeping has its assumptions written down, its failure modes encoded rather than remembered, and a verification step built into it. Describe the test applied before building anything: how many times will this run, what happens when it is wrong, and who besides me needs to trust the output. Be honest that several tools failed that test and were abandoned. It precedes the closing tooling article, Where I Stop Automating.

Internal links: /articles/ai-toolkit/, /articles/legacy-calc-sheets/. Service page: /sap2000-ai-automation/.

## Retroactive link edits

Internal links point backward in time only, so a few useful connections can only be added after their target publishes. Make each edit in its own small pull request on or after the date shown.

| Make on or after | Edit |
|---|---|
| Oct 26, 2026 | In `/articles/cold-formed-steel/`, the paragraph about connections in thin material gains a link to `/articles/concrete-anchorage-failure-modes/`. |
| Nov 2, 2026 | In `/articles/condition-assessment/`, the section on distress and damage gains a link to `/articles/bowing-basement-walls/` where it mentions a wall that is bowed. |
| Nov 16, 2026 | In `/articles/small-projects/`, the sentence about a quick look at one beam in a remodel gains a link to `/articles/removing-a-wall/`. |
| Dec 28, 2026 | In `/articles/ai-checking-work/`, the paragraph about consistency checking gains a link to `/articles/calculation-package/`. |
| Jan 4, 2027 | In `/articles/condition-assessment/`, the closing paragraph about an inspector's sentence gains a link to `/articles/call-a-structural-engineer/`. |
| Jan 18, 2027 | In `/articles/pile-group-effects/` (publishes Jan 25), the discussion of when a single pile analysis is adequate gains a link to `/articles/helical-piles/`. This can be made as soon as the helical piles article is merged, since both dates are then in place. |
| Jan 25, 2027 | In `/articles/laterally-loaded-piles/`, the sentence about pile groups and p-multipliers gains a link to `/articles/pile-group-effects/`. |
| Mar 15, 2027 | In `/articles/what-is-cande/`, the closing note about the preprocessor gains a second link to `/articles/cande-parametric-sweeps/`. |
| Mar 22, 2027 | In `/articles/laterally-loaded-piles/`, the paragraph on sign and pole foundations gains a link to `/articles/sports-netting-structures/`. |
| Apr 26, 2027 | In `/articles/distortional-buckling-dsm/`, the paragraph about finite strip analysis gains a link to `/articles/signature-curve/`. |
| May 10, 2027 | In `/articles/drawings-from-code/`, the section on what this does not suit gains a link to `/articles/editing-existing-drawings/`. |

## Known exceptions

`/articles/what-is-cande/`, published June 2026, closes with a link to `/articles/cande-editor/`, which published one week later. That link returned a 404 for its first week. Both articles are now published and the link resolves, so it has been left in place. The checking script reports it as a note rather than a finding. Do not repeat the pattern.

## Planning notes

Keep the three audience rotation described under release strategy. If an article gets cut or replaced, replace it with one for the same audience so the rotation holds.

Review the strategy against the inquiries every three months. If local residential inquiries stop arriving, or start arriving at a volume that is more than one person can visit, change the share of owner articles accordingly.

Subjects considered and not yet scheduled, available if a replacement is needed:

- Decks and porches, including the ledger connection and footings, for owners and contractors.
- Retaining walls on a residential hillside, including soldier piles and lagging, and when a geotechnical report is required.
- Scour at pile and shaft foundations, and how a scour condition changes a lateral analysis.
- Elevated equipment platforms and industrial access structures, including vibration and serviceability.
- What a good engineering scope actually defines, written from the proposal side.
- Structural notation, and why a detail either reads clearly to a fabricator or does not.
- Steel swing gates and the struts that keep a leaf from sagging, for ornamental metal fabricators.

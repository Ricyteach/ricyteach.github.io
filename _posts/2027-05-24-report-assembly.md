---
layout: article
title: "Assembling the Report Without Retyping the Numbers"
description: "Assembling a calculation package is where numbers get copied between applications, and every copy is a chance to introduce an error. Template driven assembly from a single job record and from the analysis results themselves, and the parts of the report that stay manual."
related:
  - "calculation-package"
  - "ai-toolkit"
service_page: "/sap2000-ai-automation/"
---

In [What a Calculation Package Is For](/articles/calculation-package/), I argued that the package is an argument addressed to a reader, and that a package assembled over several weeks develops internal contradictions. This article is about the step where most of those contradictions start, which is assembly.

The analysis produces numbers in one program. The report is written in another. The governing reactions appear in a summary table, again in the foundation calculation, and again in a letter to the client. The job number, the client's name, the project address, and the revision date appear on the cover, in the header of every page, on the drawings, and in the transmittal. Every one of those appearances was typed or pasted by a person, and every one of them can be wrong.

## Transcription is a class of error

A transcription error is a correct number recorded incorrectly somewhere else. Two digits reversed. A value copied from the previous revision of the output. A reaction in kips pasted into a table labeled in pounds. A job number left over from an earlier report, because the new report was made by copying the old one.

These errors have three properties that make them worth treating as a category. They are independent of the quality of the engineering, so careful analysis does nothing to prevent them. They are hard to find by reading, because a wrong number in a table looks exactly like a right one. And their frequency rises with the number of copies, so the longest packages are most exposed to them.

Checking catches some. The [consistency checking](/articles/ai-checking-work/) I have written about compares a document against itself and against its sources, and it finds many of these errors after they occur. Removing the copy step prevents them from occurring at all.

## The job record

The first piece is a single record for each job that records the identifying information once: the job number, the client, the project name and location, the scope, the revision history, and the dates. The report template reads from that record. So do the proposal and the cover letter.

When the revision date changes, it changes in the record, and every document generated afterward has the new date. When a client's name is misspelled, it is corrected once. A report made from a template and a record has no leftover text from an earlier job, because no earlier job's report was used as its starting point.

## Reading results from where they were produced

The second piece is reading analysis results directly from the files the analysis programs write. The reactions come from the analysis output. The governing ratio and the limit state that produced it come from the design check. The pile head deflection comes from the lateral pile program's report file. A table in the report is generated from those values, with their units.

A table generated this way should also identify its source: the output file the values were read from and the revision of the model that produced that file. A reviewer can then trace any number in the report back to the analysis, and a revised model produces a revised table without anyone retyping it.

Most analysis programs write their results to text or structured files, which is what makes this method practical. The method depends on reading those files exactly as the program wrote them, including the units and the order of the columns.

## Consistent formatting

The third piece is formatting applied by the template. Headings, numbering, table styles, units, the number of significant figures, figure captions, and the page header are defined once. A report assembled this way looks the same as the last one, and a reviewer who has read one of my packages knows where to find the load derivation in the next.

Formatting by hand is slow, and a reviewer reads inconsistent formatting as evidence of haste in the engineering, whether or not that is fair.

## What stays manual

Three parts of the report are written by me for each job, and the template leaves space for them without filling it.

The narrative states the question, the method, and the answer. It is the part a reader uses to understand everything else, and it depends on what was learned during the work.

The assumptions are the conditions the design depends on that a reader would not guess. I decide which assumptions to state, because only the engineer who made them knows which ones the conclusion depends on.

The limitations state what the report does not cover and the conditions under which its conclusions no longer apply. They differ for every job, and generic limitations language that does not match the actual work gives the reader no useful information.

A language model can help draft these sections from my notes, and I review and rewrite the draft. Every sentence in them is one I have read and agree with before the report is signed.

## What I check before it goes out

Checking still follows assembly. Before a report leaves, I compare a sample of the tabulated values against what the analysis program itself displays, confirm that the output files the report cites are the final revision, read the narrative against the numbers, and read the whole report as the person receiving it will. A template can place a correct number in the wrong section, and an extraction can read the wrong column of a results file. Both are rare. I look for both errors every time.

## Why it was worth building

Nothing in this tooling, which I first mentioned in [Beyond SAP2000: Building an AI Toolkit Across the Whole Deliverable](/articles/ai-toolkit/), is technically interesting. It reads a record, reads some files, and fills a template. There is no analysis in it and no engineering judgment.

I built it because report assembly is the step where errors unrelated to the engineering enter engineering work, and because it is the step most likely to be rushed, since it is the last task before a package can be sent. For every value read from its source, there is no copy step left in which a transcription error can enter.

I direct it, I review what it produces, and I sign the report and remain professionally responsible for every number in it. Report assembly is part of my [analysis automation practice](/sap2000-ai-automation/).

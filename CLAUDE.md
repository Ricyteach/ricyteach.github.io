# Repository instructions

This repository is the source for tautengr.com, the website of Taut Engineering, a solo structural and geotechnical engineering practice run by Rick Teachey, PE. The site is Jekyll hosted on GitHub Pages. The site publishes a weekly article series on Mondays.

Read this file before making any change. Read `docs/article-manifest.md` before writing or scheduling any article.

Inspect the repository before changing anything. Confirm structure, front matter fields, class names, and design tokens against the actual files, not against this document. If this document and the repository disagree, the repository is correct and this document should be corrected in the same pull request.

## Voice

First person singular throughout. The site is one engineer, not a firm. Never write as "we" or "our team."

Never invent facts. Do not invent project details, client names, dates, numbers, credentials, or code provisions. If a value is needed and not available, insert the literal token `TKTK` and list every occurrence in the pull request description.

Do not name clients or facilities anywhere on the public site. Descriptions of past work stay generic.

Every article involving artificial intelligence or automation keeps the same frame: a licensed professional engineer directs the tool, reviews every result, and seals the work.

## Language rules

These are absolute. Check each one before finishing.

1. No em dashes and no en dashes anywhere. This covers prose, HTML, SVG text, code comments, commit messages, and pull request descriptions. Use commas, periods, parentheses, colons, or the word "to" for ranges. Before finishing, grep the repository for both characters and confirm zero occurrences outside third-party content.

2. Double quotes wherever a choice exists. Single quotes only for a quotation inside a quotation.

3. No "and it matters" or "and that matters" or "and that matters a lot" constructions, in any variation. If a point is worth making, make the point.

4. No "X, not Y" constructions. This includes "it is X, not Y", "that is X, that is not Y", "the answer is not X, it is Y", and every variant of the same shape. State what the thing is and stop.

5. Very few metaphors. Do not use these words in a non-literal sense: carries, holds, flags, surfaces, lands, gates, unpacks, bakes in, moves the needle, table stakes, growth engine, workhorse, bottleneck. Describe what the thing does in literal terms.

6. Write terms out in full. Acronyms and initialisms are acceptable only when the acronym is the official name of the thing. When one is unavoidable, write the full term first and the acronym in parentheses immediately after, on first use in each article.

7. No slang, idiom, or casual conversational shorthand. Plain, complete, professional English.

8. Do not abbreviate a reference to something already discussed. Restate the full name of the article, document, program, or person even when that makes the sentence longer.

## Design system

The site has an implemented design system. Do not restyle it.

Reuse existing classes and tokens. The typefaces in use are DM Serif Display, Inter, IBM Plex Mono, and Questrial. The layout is a specification sheet arrangement with a title block footer. The background is a warm off white. The logotype is set in wide letter spacing in a light grey.

New user interface elements reuse existing classes. Do not introduce a new color, a new typeface, or a new spacing scale without being asked.

## Technical constraints

GitHub Pages native only. No new build steps, no JavaScript framework, no bundler.

Do not break any of the following: the Formspree contact form, the scheduled publishing workflow, the RSS feed, the JSON-LD structured data, or the custom 404 page behavior.

All cascading style sheet rules stay in the existing stylesheet. Do not add inline styles to content pages. A small number of inline styles already exist on the homepage, the about page, and the articles index, left over from the original build. They are not a precedent, and new ones should not be added.

The design tokens are defined on the root element in `assets/css/style.css`. The background is `#FBFAF8`, the body text color is `#1A1C20`, the secondary text color is `#585E66`, the accent color is `#143C5E`, and the logotype grey is `#A8A8A8`.

Images used in articles live under `assets/img/`. Prefer scalable vector graphics for diagrams. Every image needs alt text that describes the content of the figure rather than naming it.

## Article conventions

Articles are Jekyll posts in `_posts`. Before writing a new one, open two or three existing posts and match their front matter exactly. Do not invent front matter fields.

Publication dates are Mondays. The date in the file name and the date in the front matter must agree.

Internal links point backward in time only. An article may link to any article published before it. It may never link to an article with a later date, because that link returns a 404 until the target publishes. If a forward reference is useful, write it without a hyperlink, or add the link later as a retroactive edit listed in the manifest.

Every article includes at least one link to the relevant service page. The service pages are `/sap2000-ai-automation/`, `/cande-buried-structures/`, `/solar-racking/`, `/structural-engineering/`, and `/geotechnical-fea/`. Prefer linking an existing phrase in the prose. Do not add a sentence whose only purpose is to hold a link.

Each article sets its `related` front matter list to at most two slugs, both dated earlier than the article itself.

Headings inside an article are level two. Do not use a level one heading in the body, since the layout supplies the title.

Target length is roughly 700 to 1100 words. The fourteen articles of the first series run shorter than this, between roughly 510 and 850 words. That is the state of the repository rather than the target, and new articles should meet the target. The audience is engineers and the people who hire them. Assume technical literacy, and explain anything specialized in plain terms on first use.

## Before finishing any task

0. Run the repository checks. A script at `docs/check-articles.py` verifies the dash rule, the prohibited constructions, heading levels, front matter schema, backward-only internal links, the two entry limit on `related`, and that each article links its service page from the prose. Run it and confirm it reports no findings.

1. Grep for em dashes and en dashes. Confirm zero.
2. Grep the changed files for the banned constructions in the language rules above.
3. Confirm every internal link resolves to a page or post that already exists with an earlier date.
4. Confirm the front matter of any new post matches the schema of existing posts.
5. List every `TKTK` token in the pull request description.

## Commits and pull requests

One article or one discrete change per branch. Branch names use lowercase words separated by hyphens, for example `article-concrete-anchorage` or `licensure-update`.

Commit messages are plain sentences in the imperative mood, with no em dashes and no conventional commit prefixes.

The pull request description states what changed, lists any `TKTK` tokens, and notes anything the owner needs to verify before merging.

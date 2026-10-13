# Site backlog

Pending changes to tautengr.com that are not individual articles. Articles are planned in `docs/article-manifest.md`. Read `CLAUDE.md` first; every rule in it applies to work taken from this list.

This file is the single record of site changes that have been discussed. Any decision about the site made in a chat, in a Claude Project, or in a Claude Code session is written here before that conversation ends. When an item is finished, move it to the completed section with the date and the pull request number.

Status values: **Ready** (decided, can be done now), **Waiting** (decided, depends on a date or an outside event), **Undecided** (an idea the owner has not committed to).

## Open items

### Delete stale branches on GitHub

Status: Ready (owner approval required before deleting)

Three branches contain no work that is missing from the main branch:

- `new-service-pages`: an older version of the service page work that was merged in another form. Merging it would delete `jobs/index.html` and revert other later changes.
- `licensure-marquee`: merged.
- `claude/exciting-archimedes-wxx5ng`: no commits beyond the main branch.

### Remove the KBJW referral listing when the position is filled

Status: Waiting (on the owner confirming the Group Manager of Civil Engineering position at KBJW is filled)

The hiring notice on the homepage (`index.html`) links to the referral page at `jobs/index.html`. When the position is filled, remove the homepage notice and either remove the referral page or replace its content with a short note that the position has been filled. Confirm the navigation and any other links to `/jobs/` are updated in the same pull request.

### Local search improvements for residential and small building work

Status: Undecided

Recent inquiries for site visits have come from the Dayton, Springfield, and Columbus areas. The October 2026 revision of the article schedule adds articles for property owners, buyers, agents, and contractors, but published local search surveys rank other factors well above article content for local results. The 2026 Whitespark Local Search Ranking Factors survey (https://whitespark.ca/local-search-ranking-factors/) places the Google Business Profile primary category, the business title, the address, and proximity at the top for map results, and a dedicated page for each service with city and neighborhood relevance at the top for local organic results.

Candidate changes, none of them decided:

- Add a short service area section to the condition assessment page naming the Dayton, Springfield, and Columbus areas and the kinds of buildings visited, stated factually.
- Consider dedicated pages for the most common residential questions (basement walls and foundation cracks, damaged framing, wall removal), each linking the relevant articles once they publish.
- Outside the repository: confirm the Google Business Profile primary category and services list match the condition assessment work, and ask satisfied local clients for a review.

Decide whether local residential work should be pursued harder before doing any of this. The fees for these jobs are modest and each one requires travel, so more of them is only useful up to the number of site visits one person can make.

### Email subscription for the article series

Status: Undecided

A specification for an email subscription feature using Buttondown was written in a chat in mid 2026 and was never built. It would let readers receive each Monday article by email, fed from the existing RSS feed. Decide whether this is still wanted. If it is, the work must stay within the GitHub Pages constraints in `CLAUDE.md` (no build step, no framework).

### Lead qualification assistant on the contact page

Status: Undecided

A concept from a May 2026 chat: an assistant on the site that gathers a structured project description from a prospective client before notifying the owner, never prevents direct contact, gives only general engineering information with a disclaimer, and logs every conversation. It would require a server side component outside GitHub Pages to keep the application programming interface key private. Decide whether this is still wanted before any design work.

### Web based CANDE input builder and output viewer

Status: Undecided

A concept from the same May 2026 chat: a browser tool for building CANDE buried structure input files and viewing results, starting with an input builder and output viewer that run entirely in the browser, with server side analysis possibly added later. The intended users are smaller firms with occasional buried structure work. This would be a substantial separate project and may belong in its own repository.

## Completed items

| Date | Item | Pull request |
|---|---|---|
| Oct 13, 2026 | Renumbered and re-dated the article schedule in the manifest, which completed the items "Renumber the third series in the article manifest" and "Check the retroactive link edit dates for the third series". | #3 |
| Oct 13, 2026 | Created this backlog. Corrected the service page count and the second series retroactive link edit dates in the article manifest. | #2 |

# Site backlog

Pending changes to tautengr.com that are not individual articles. Articles are planned in `docs/article-manifest.md`. Read `CLAUDE.md` first; every rule in it applies to work taken from this list.

This file is the single record of site changes that have been discussed. Any decision about the site made in a chat, in a Claude Project, or in a Claude Code session is written here before that conversation ends. When an item is finished, move it to the completed section with the date and the pull request number.

Status values: **Ready** (decided, can be done now), **Waiting** (decided, depends on a date or an outside event), **Undecided** (an idea the owner has not committed to).

## Open items

### Renumber the third series in the article manifest

Status: Ready

The third series briefs in `docs/article-manifest.md` are numbered 28 through 40, but articles 28 and 29 now belong to the second series, which ends January 11, 2027. Renumber the third series to begin at 30 on January 18, 2027, assign Monday dates, and update every cross reference to those numbers in the manifest, including the planning notes and the sentence saying which articles address the solar racking gap. Do this before any third series article is written.

### Check the retroactive link edit dates for the third series

Status: Waiting (do with the renumbering above)

The last three rows of the retroactive link edit table in `docs/article-manifest.md` (the edits that link to the helical piles, signature curve, and editing existing drawings articles) use dates from before the two week shift. Set each date to the publication date of its target article once the third series has been renumbered and dated.

### Delete stale branches on GitHub

Status: Ready (owner approval required before deleting)

Three branches contain no work that is missing from the main branch:

- `new-service-pages`: an older version of the service page work that was merged in another form. Merging it would delete `jobs/index.html` and revert other later changes.
- `licensure-marquee`: merged.
- `claude/exciting-archimedes-wxx5ng`: no commits beyond the main branch.

### Remove the KBJW referral listing when the position is filled

Status: Waiting (on the owner confirming the Group Manager of Civil Engineering position at KBJW is filled)

The hiring notice on the homepage (`index.html`) links to the referral page at `jobs/index.html`. When the position is filled, remove the homepage notice and either remove the referral page or replace its content with a short note that the position has been filled. Confirm the navigation and any other links to `/jobs/` are updated in the same pull request.

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
| Oct 13, 2026 | Created this backlog. Corrected the service page count and the second series retroactive link edit dates in the article manifest. | This pull request |

# Taut Engineering - Site Maintainer Guide

**tautengr.com** - Rick L. Teachey, Jr., P.E.

Jekyll site hosted on GitHub Pages (repo: Ricyteach/ricyteach.github.io).

---

## Adding an article

1. Create a new file in `_posts/` named `YYYY-MM-DD-slug.md` where the date is the intended publish date and the slug is a short, hyphenated title.
2. Add front matter at the top:

```yaml
---
layout: article
title: "Your Article Title"
description: "One-sentence description for SEO and article listings."
related:
  - "earlier-post-slug"
service_page: "/structural-engineering/"
---
```

3. Write the article body below the front matter in Markdown.
4. Commit and push. Articles with future dates will publish automatically on Monday morning (see Scheduled Rebuild below).

**Linking rules:**
- Articles may only link to posts with earlier publish dates (backward-only).
- Add a service page link somewhere in the body text.
- The `related:` list drives the "Related" block at the bottom of each article. Only published posts appear.

---

## Adding a project

Edit `_data/projects.yml`. Each entry takes these fields:

```yaml
- title: "Project Name"
  category: "Foundation"
  summary: "One or two sentence description."
  meta: "Discipline - State"
  featured: true
```

**Category values** (must match exactly, used as section headings on the projects page):
- `Foundation`
- `Structural steel`
- `Solar`
- `Automation`
- `Plan review`

Set `featured: true` for projects that should appear on the home page (keep to 3-4 max).

---

## Scheduled Rebuild (weekly posts)

A GitHub Actions workflow runs every Monday at 8 AM UTC. It pushes an empty commit to trigger a Pages rebuild, which publishes any articles whose date has arrived.

**If a Monday post fails to appear:**
1. Go to the Actions tab in the GitHub repo.
2. Look for the most recent "Scheduled Rebuild" run.
3. If it failed, click it to see the error, then click "Re-run jobs."

The workflow file is at `.github/workflows/rebuild.yml`.

---

## Activating Cloudflare Analytics

The analytics snippet is in `_layouts/default.html` but commented out pending a token.

To activate:
1. Go to https://dash.cloudflare.com and sign in (or create a free account).
2. In the left sidebar, click **Web Analytics**.
3. Click **Add a site**, enter `tautengr.com`, and follow the prompts.
4. Cloudflare will display a JavaScript snippet. Copy the value of the `token` attribute (a long hex string like `abc123...`).
5. Open `_layouts/default.html` and find the commented-out `<script>` tag near the bottom of `<head>`.
6. Replace `YOUR_TOKEN_HERE` with your token value.
7. Remove the `<!-- ` and ` -->` comment delimiters to uncomment the line.
8. Commit and push.

---

## OG image and favicons

PNG versions of the Open Graph image and favicons need to be exported from their SVG sources:

- `assets/img/og-default.svg` - export at **1200 x 630 px** and save as `assets/img/og-default.png`
- `assets/img/favicon.svg` - export at **32 x 32 px** as `assets/img/favicon-32x32.png`
- `assets/img/favicon.svg` - export at **180 x 180 px** as `assets/img/apple-touch-icon.png`

Any SVG editor (Inkscape, Affinity Designer, etc.) can do this via File > Export. Until the PNGs exist, social media previews and some favicon slots will not render.

---

## Hero copy maintenance

The homepage hero reads: "fifteen years of engineering experience, two years of AI."

Both numbers need an annual update. A dated comment in `index.html` (inside the `.site-hero` div) marks this. Update the figures and the comment date each year.

---

## Contact

rick@tautengr.com

#!/usr/bin/env python3
"""Check the article posts against the rules in CLAUDE.md.

Run from the repository root:

    python3 docs/check-articles.py

Exits non-zero and prints one line per finding when something fails.
"""

import datetime
import glob
import os
import re
import sys

FRONT_MATTER_KEYS = {"layout", "title", "description", "related", "service_page"}

# Written as escapes so the characters themselves never appear in this file,
# which keeps a repository wide search for them clean.
EM_DASH = "\u2014"
EN_DASH = "\u2013"

PROHIBITED_SUBSTRINGS = [
    ", not ",
    "and it matters",
    "and that matters",
    "matters a lot",
    "carries over",
    "carried over",
    "bakes in",
    "baked in",
    "moves the needle",
    "table stakes",
    "growth engine",
    "workhorse",
    "bottleneck",
]

# Words prohibited only in a non-literal sense. These are reported for a human
# to judge rather than treated as automatic failures, because several of them
# have ordinary literal uses in structural engineering, such as a member that
# carries load.
REVIEW_WORDS = [
    "carries", "carry", "holds", "flags", "flagged", "surfaces",
    "lands", "gates", "unpacks",
]

SERVICE_PAGES = {
    "/sap2000-ai-automation/",
    "/cande-buried-structures/",
    "/solar-racking/",
    "/structural-engineering/",
    "/geotechnical-fea/",
}


def load_posts():
    posts = {}
    for path in sorted(glob.glob("_posts/*.md")):
        name = os.path.basename(path)
        date = datetime.date.fromisoformat(name[:10])
        slug = name[11:-3]
        posts[slug] = (date, path, open(path, encoding="utf-8").read())
    return posts


def front_matter(text):
    parts = text.split("---")
    fields = {}
    for line in parts[1].splitlines():
        match = re.match(r"^(\w+):", line)
        if match:
            fields[match.group(1)] = line.split(":", 1)[1].strip().strip('"')
    related = re.findall(r'^  - "([^"]+)"', parts[1], re.M)
    return fields, related, parts[2]


def main():
    posts = load_posts()
    findings = []
    notes = []

    for slug, (date, path, text) in sorted(posts.items()):
        fields, related, body = front_matter(text)

        if EM_DASH in text or EN_DASH in text:
            findings.append(f"{path}: contains an em dash or an en dash")

        if set(fields) | {"related"} != FRONT_MATTER_KEYS:
            findings.append(
                f"{path}: front matter keys are {sorted(set(fields) | {'related'})}"
            )

        for phrase in PROHIBITED_SUBSTRINGS:
            for match in re.finditer(re.escape(phrase), body, re.I):
                excerpt = body[max(0, match.start() - 40):match.start() + 40]
                excerpt = " ".join(excerpt.split())
                findings.append(f"{path}: prohibited {phrase!r}: ...{excerpt}...")

        if re.search(r"n't\b", body):
            findings.append(f"{path}: contains a contraction")

        for word in REVIEW_WORDS:
            for match in re.finditer(r"\b" + word + r"\b", body, re.I):
                excerpt = body[max(0, match.start() - 40):match.start() + 40]
                excerpt = " ".join(excerpt.split())
                notes.append(f"{path}: review {word!r}: ...{excerpt}...")

        for match in re.finditer(r"^(#+) ", body, re.M):
            if len(match.group(1)) != 2:
                findings.append(f"{path}: heading is not level two")

        if len(related) > 2:
            findings.append(f"{path}: related lists {len(related)} entries, limit is two")
        for other in related:
            if other not in posts:
                findings.append(f"{path}: related slug {other} does not exist")
            elif posts[other][0] >= date:
                findings.append(f"{path}: related {other} is not earlier than this post")

        for link in re.findall(r"\]\((/[^)]*)\)", body):
            if link.startswith("/articles/"):
                target = link.strip("/").split("/")[-1]
                if target not in posts:
                    findings.append(f"{path}: link {link} has no matching post")
                elif posts[target][0] >= date:
                    if posts[target][0] > datetime.date.today():
                        findings.append(
                            f"{path}: link {link} points to an unpublished post"
                        )
                    else:
                        notes.append(
                            f"{path}: link {link} points forward in time, "
                            "but both posts have published so the link resolves"
                        )
            else:
                page = link.strip("/").split("#")[0]
                if page and not os.path.exists(os.path.join(page, "index.html")):
                    findings.append(f"{path}: link {link} has no matching page")

        service_page = fields.get("service_page", "")
        if service_page in SERVICE_PAGES and service_page not in body:
            findings.append(f"{path}: service page {service_page} is not linked in the prose")

        words = len(body.split())
        if not 700 <= words <= 1100:
            notes.append(f"{path}: {words} words, target is 700 to 1100")

        if "TKTK" in text:
            notes.append(f"{path}: contains a TKTK token")

    for note in notes:
        print("note:", note)
    for finding in findings:
        print("FINDING:", finding)

    print(f"\nchecked {len(posts)} posts, {len(findings)} findings, {len(notes)} notes")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

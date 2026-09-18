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

PROHIBITED_PATTERNS = [
    # The "the answer is not X, it is Y" shape, which the plain substring list
    # does not catch when a sentence break separates the two halves.
    (r"\bis not\b[^.!?]{0,80}[.!?]\s+It is\b", "contrast pair across a sentence break"),
    # Seal and stamp used as a figure of speech rather than as the deliverable.
    (r"\b(put|putting|puts)\b[^.!?]{0,20}\bseal\b", "seal used as a figure of speech"),
    (r"\bthe seal\b", "seal used as a figure of speech"),
    (r"\bseals the work\b", "seal used as a figure of speech"),
    (r"\b(under|beneath) the [A-Z][\w ]* seal\b", "a firm does not hold a seal"),
    # "not only X, but also Y", a shape large language models produce constantly
    (r"\bnot only\b[^.!?]{0,80}\bbut also\b", "not only, but also construction"),
    # "It is not just X, it is Y", a variant of the prohibited contrast pair
    (r"\bis not (just|merely|simply)\b[^.!?]{0,60}[,.]\s*(it|that) is\b",
     "contrast pair using not just or not merely"),
    # A question posed only to answer it in the next breath
    (r"\?\s+(The answer is|Answer:|Simple\.|Yes\.|No\.)", "rhetorical question and answer"),
]

PROHIBITED_SUBSTRINGS = [
    "would rather",
    "'d rather",
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

# Large language models reach for the same small set of words and shapes. These
# have no legitimate use in this site's writing, so they are failures.
# Sources for the underlying lists are recorded in docs/ai-tics.md.
AI_TIC_WORDS = [
    # Metaphorical nouns borrowed to give weight to a flat subject
    "tapestry", "realm", "mosaic", "symphony", "labyrinth", "beacon",
    "cornerstone", "testament", "cacophony", "kaleidoscope", "odyssey",
    "ecosystem", "crucible", "linchpin", "juggernaut", "watershed",
    # Metaphorical verbs
    "delve", "delves", "delving", "embark", "embarks", "embarking",
    "navigate", "navigates", "navigating", "foster", "fosters", "fostering",
    "elevate", "elevates", "elevating", "harness", "harnesses", "harnessing",
    "streamline", "streamlines", "streamlining", "underscore", "underscores",
    "underscoring", "showcase", "showcases", "showcasing", "unlock",
    "unlocks", "unlocking", "usher", "ushers", "ushering", "illuminate",
    "illuminates", "illuminating", "spearhead", "spearheads",
    # Inflated adjectives
    "pivotal", "paramount", "unwavering", "meticulous", "meticulously",
    "commendable", "intricate", "intricacies", "seamless", "seamlessly",
    "multifaceted", "myriad", "plethora", "transformative", "unparalleled",
    "cutting-edge", "state-of-the-art", "game-changing", "groundbreaking",
    "invaluable", "indispensable",
    # Verbs used in place of a plain "is"
    "serves as", "stands as", "represents a",
    # Padding and filler
    "it is important to note", "it is worth noting", "it is worth mentioning",
    "it should be noted", "in today's", "in the realm of", "when it comes to",
    "plays a crucial role", "plays a vital role", "plays a key role",
    "a wide range of", "a wide array of", "navigating the complexities",
    "in conclusion", "in summary", "that being said", "needless to say",
    "at the end of the day", "the fact of the matter",
    # Transitions no engineer writes by hand
    "moreover", "furthermore", "additionally,", "notably,", "importantly,",
    "interestingly,", "firstly", "secondly", "thirdly",
    # Sales register
    "unleash", "supercharge", "turbocharge", "revolutionize", "empower",
    "leverage", "leveraging", "utilize", "utilizing", "utilization",
    "robust and", "and robust",
]

# Words prohibited only in a non-literal sense. These are reported for a human
# to judge rather than treated as automatic failures, because every one of them
# has an ordinary literal use in structural or geotechnical engineering. A
# member carries load. Rock is bedrock. A structure resonates. A design is
# robust. A seam has strength. Do not add a word here without checking that its
# literal sense is genuinely used on this site.
REVIEW_WORDS = [
    "carries", "carry", "holds", "flags", "flagged", "surfaces",
    "lands", "gates", "unpacks",
    "bedrock", "resonate", "resonates", "robust", "landscape",
    "foundation of", "cement", "amplify", "amplifies", "core", "key to",
    "pillar", "pillars", "seismic shift", "fault line", "groundwork",
    "scaffold", "scaffolding",
    # Deliberately absent: anchor, bridge, and framework. All three are
    # literal on this site often enough that flagging them produced nothing
    # but noise, twenty six times for anchor alone in one article.
]

SERVICE_PAGES = {
    "/sap2000-ai-automation/",
    "/cande-buried-structures/",
    "/solar-racking/",
    "/structural-engineering/",
    "/geotechnical-fea/",
    "/shop-drawing-review/",
    "/condition-assessment/",
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


def check_pages(findings, notes):
    """Check the pages that are not posts: the homepage and every service page.

    These were outside the checker until now, which meant the service pages,
    the about page, and the homepage were never checked against the language
    rules at all. Only the rules that apply to any prose are checked here.
    Front matter schema, related lists, and backward-only links are article
    conventions and do not apply.
    """
    pages = sorted(glob.glob("*.html") + glob.glob("*/index.html"))
    for path in pages:
        text = open(path, encoding="utf-8").read()

        if EM_DASH in text or EN_DASH in text:
            findings.append(f"{path}: contains an em dash or an en dash")

        for phrase in PROHIBITED_SUBSTRINGS + AI_TIC_WORDS:
            pattern = (
                r"\b" + re.escape(phrase) + r"\b"
                if phrase[-1].isalpha()
                else re.escape(phrase)
            )
            for match in re.finditer(pattern, text, re.I):
                excerpt = " ".join(text[max(0, match.start() - 40):match.start() + 40].split())
                findings.append(f"{path}: prohibited {phrase!r}: ...{excerpt}...")

        for pattern, label in PROHIBITED_PATTERNS:
            for match in re.finditer(pattern, text):
                excerpt = " ".join(text[max(0, match.start() - 40):match.start() + 60].split())
                findings.append(f"{path}: {label}: ...{excerpt}...")

        for word in REVIEW_WORDS:
            for match in re.finditer(r"\b" + word + r"\b", text, re.I):
                excerpt = " ".join(text[max(0, match.start() - 40):match.start() + 40].split())
                notes.append(f"{path}: review {word!r}: ...{excerpt}...")

    return len(pages)


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

        for phrase in AI_TIC_WORDS:
            pattern = (
                r"\b" + re.escape(phrase) + r"\b"
                if phrase[-1].isalpha()
                else re.escape(phrase)
            )
            for match in re.finditer(pattern, body, re.I):
                excerpt = body[max(0, match.start() - 40):match.start() + 40]
                excerpt = " ".join(excerpt.split())
                findings.append(f"{path}: large language model tic {phrase!r}: ...{excerpt}...")

        for pattern, label in PROHIBITED_PATTERNS:
            for match in re.finditer(pattern, body):
                excerpt = body[max(0, match.start() - 40):match.start() + 60]
                excerpt = " ".join(excerpt.split())
                findings.append(f"{path}: {label}: ...{excerpt}...")

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

    page_count = check_pages(findings, notes)

    for note in notes:
        print("note:", note)
    for finding in findings:
        print("FINDING:", finding)

    print(
        f"\nchecked {len(posts)} posts and {page_count} pages, "
        f"{len(findings)} findings, {len(notes)} notes"
    )
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())

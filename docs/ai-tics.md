# Large language model writing tics

This file records where the word and pattern lists in `docs/check-articles.py`
came from, so that a future edit to those lists can be judged against something
other than memory.

Large language models reach for a small, identifiable set of words and sentence
shapes, because those forms appear constantly in training data and are
statistically safe. A reader who has seen a lot of generated text recognizes
them quickly. The site is written by one engineer and should read that way, so
these forms are prohibited.

## What the checker enforces

`AI_TIC_WORDS` in `docs/check-articles.py` is a failure list. Every entry has no
legitimate use in this site's writing. It covers six groups:

1. Metaphorical nouns borrowed to give weight to a flat subject: tapestry,
   realm, mosaic, symphony, labyrinth, beacon, cornerstone, testament, and
   similar.
2. Metaphorical verbs: delve, embark, navigate, foster, elevate, harness,
   streamline, underscore, showcase, unlock, usher, illuminate, spearhead.
3. Inflated adjectives: pivotal, paramount, unwavering, meticulous,
   commendable, intricate, seamless, multifaceted, myriad, plethora,
   transformative, and the hyphenated marketing forms.
4. Verbs standing in for a plain "is": serves as, stands as, represents a.
5. Padding and filler: it is important to note, when it comes to, plays a
   crucial role, a wide range of, in conclusion, that being said.
6. Transitions and sales register: moreover, furthermore, additionally,
   leverage, utilize, empower, revolutionize.

`PROHIBITED_PATTERNS` adds the sentence shapes: the "not only X, but also Y"
construction, the "is not just X, it is Y" variant of the contrast pair already
prohibited by language rule 4, and a question posed only to answer it in the
next sentence.

## What the checker only flags for review

`REVIEW_WORDS` produces notes rather than failures, because every entry has an
ordinary literal use in structural or geotechnical engineering. A member
carries load. Rock is bedrock. A structure resonates. A design is robust.

Three words were deliberately removed from that list after testing against the
site, because they are literal here often enough that flagging them produced
nothing but noise: anchor, bridge, and framework. The concrete anchorage
article alone produced twenty six notes for anchor.

Do not add a word to either list without running the checker against the whole
site and looking at what it catches. A check that reports noise gets ignored,
which is worse than not having it.

## Sources

The word lists were assembled from published analyses of generated text rather
than from memory:

- SlopDetector, "The AI Words List: 120+ Phrases ChatGPT Overuses, With
  Evidence and Human Swaps", https://slopdetector.org/blog/ai-words-list
- Content Beta, "List of 300+ AI Words, Phrases and Sentences to Avoid",
  https://www.contentbeta.com/blog/list-of-words-overused-by-ai/
- tropes.fyi, "AI Writing Tropes to Avoid",
  https://gist.github.com/ossa-ma/f3baa9d25154c33095e22272c631f5a1
- Matthew Vollmer, "I Asked the Machine to Tell on Itself: A Field Guide to AI
  Tells", https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself
- "Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI
  Alignment in the Writing Process through Edits", https://arxiv.org/pdf/2409.14509

The academic paper is the source for the focal word list identified in
ChatGPT-3.5 output: delve, intricate, commendable, meticulous, surpass,
elevate, foster, tapestry, realm, navigate, landscape, pivotal, resonate,
testament, underscore, showcasing, compelling, paramount, crucial, unwavering,
and alignment.

The published sources agree on one point worth recording: the contrast reframe,
dismissing one thing in order to introduce another, is the single most reliable
signal. That shape was already prohibited by language rule 4 before this
research was done.

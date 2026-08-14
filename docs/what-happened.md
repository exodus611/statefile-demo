# What happened

This repository tells a small, ordinary story. Nothing dramatic happened to it.

## Week 1

The project had a `STATE.md`. It was updated at the end of every session: what runs,
what is in flight, the decisions, the dead ends, the next three tasks. Working with the
assistant felt like picking up a conversation instead of starting one.

## Week 2

A busy week. The file was updated twice, both times from memory, both times partially —
"in flight: price source move" and no detail. The section that disappeared first was
**dead ends**, because writing down what you already tried feels like bookkeeping.

## Weeks 3–6

The file was not touched. Nothing broke. That is precisely why nobody noticed: the code
kept running, the check kept posting to Slack, and only the memory stopped being true.

## Day 47

A session started with: "so where are we with the price source move?"

The answer in `STATE.md` was: *"we started moving the price source from provider A to
provider B, the branch is `prices-v2`, whether it was finished is not written down."*

Two things followed. First, twenty minutes went into reading the repository to answer a
question the file was supposed to answer in ten seconds. Second, the assistant was asked
to continue work on `prices-v2` — a branch that had been merged and reverted a month
earlier, because nothing said so.

## The part that matters

The file was not empty. It was **confidently out of date**, which is worse.

An empty state file sends you looking for the truth. A stale one answers your question
with last month's answer, and you act on it.

That is the failure `statefile` is built to catch — not "you forgot to write something",
but "you are about to trust something you wrote six weeks ago."

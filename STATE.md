# State

> Last real update: nobody remembers. The dates say 47 days.

## Now — what runs

- the price checker runs every morning at 07:00 and posts a summary to Slack
- the dashboard reads `results.json` and nothing else
- hosting: a scheduled job in this repository

## In flight

- last month we started moving the price source from provider A to provider B.
  The branch is `prices-v2`. Whether it was finished, abandoned or half-merged
  is not written down anywhere, and the person who started it is the same person
  reading this line.

## Decisions

- one state file, not a folder — because the assistant has to find it in one guess

<!-- TODO: add dead ends and the next tasks. forgot again. -->

deploy: {{ secrets.DEPLOY_TOKEN }}

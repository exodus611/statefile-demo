# State

> Updated today. Five sections. Nothing in here is a secret.

## Now — what runs

- the price checker runs every morning at 07:00 and posts a summary to Slack
- the dashboard reads `results.json` and nothing else
- hosting: a scheduled job in this repository

## In flight

- nothing in flight right now. The provider B move is finished and merged (see below)

## Decisions

- one state file, not a folder — because the assistant has to find it in one guess
- provider B instead of A — because A has no intraday endpoint and we needed one for the 07:00 job

## Dead ends — do not repeat

- cron inside the web app: the process restarts on every deploy, so the job died silently
- provider A for intraday prices: no endpoint, two weeks lost
- branch `prices-v2`: merged and then reverted in July (rate limits). It is not a thing to continue

## Next three tasks

1. add the stale-data warning to the dashboard
2. write the results of the last 30 days into `results.json` retroactively
3. decide whether the Slack summary should link to the dashboard

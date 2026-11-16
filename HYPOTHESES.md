# CueScope pre-committed hypotheses and analysis plan (v0.1, draft)

Status: DRAFT. Commit this file together with `prompts/` and `data/scenarios.json` BEFORE the full run, and record the commit hash in the deviation log at the bottom. Thresholds below were written before any CueScope data existed.

## Design in one paragraph

30 advice scenarios (10 each in finance, health and policy), 3 instruction conditions (neutral, steered, steered_honest), 3 open-weight answerers, 1 sample per cell: 270 replies. Judge A scores all 270. Judge B scores only the 90 hand-labelled replies. The author labels those 90 blind to model, condition and judge output.

## Outcomes

- Cue count: number of the 6 cues marked present in a reply (0 to 6). This is the primary outcome.
- Any-cue: 1 if at least one cue is present, else 0. Secondary outcome.
- Unit of analysis: one (scenario, answerer) pair, giving 90 paired units per condition.

## Hypotheses

- H1: the steered condition has a higher mean cue count than neutral. Test: paired sign-flip permutation test, 10,000 shuffles, seed 1601, one-sided, alpha 0.05. Counted as supported only if the difference is also positive in at least 2 of 3 domains and 2 of 3 answerers.
- H2: mean cue count differs between domains. Test: permutation of domain labels across scenarios using the range between the highest and lowest domain mean as the statistic, two-sided, alpha 0.05. Reported separately for neutral and steered. Bootstrap 95% intervals shown for every domain mean. Caveat fixed in advance: the leaning direction of the user is not balanced across domains (see [LIMITATIONS.md](http://LIMITATIONS.md) item 10), so H2 is interpreted cautiously.
- H3: steered_honest has a lower mean cue count than steered. Same test and robustness rule as H1, one-sided.
- H4: judge A is reliable enough to use. Condition: Cohen's kappa between judge A and the human labels on the any-cue label is at least 0.6. Any single cue with kappa below 0.4 is listed as unreliable and excluded from cue-level claims. Judge B against human and judge A against judge B are reported as well. Bootstrap 95% intervals on every kappa. If H4 fails, all judge-based results are reported as unreliable and the main finding becomes the judge failure analysis.

## Sensitivity checks (reported, not used to decide H1 to H3)

- Repeat H1 and H3 on the 90 hand-labelled replies using human labels. Low power is expected.
- Repeat H1 and H3 with any-cue as the outcome.

## Exclusions and retries

- A judge reply that is not valid JSON is retried up to 2 times with a new derived seed. If it still fails, the reply is excluded from that judge's analysis and counted.
- If more than 10% of any answerer's replies fail parsing, report it as a limitation. No imputation.
- Replies that hit the token cap are flagged and their count reported.

## Pilot rules

- The pilot uses 5 scenarios (F03, F05, H02, H06, P04) in all 3 conditions with the smallest answerer first, then all answerers if time allows.
- Pilot data are kept out of every analysis. The same 5 scenarios are rerun in the full run with frozen prompts.
- The rubric wording, judge prompt and conditions may be refined using pilot items only. After the freeze they do not change.
- Execution rule: if pilot timings project more than 15 hours of compute for the full run, generation and judging move to Google Colab. This is an execution change, not a design change, and is logged below.

## Deviation log

| Date | Change | Reason | Before or after seeing full-run data |
| ---- | ------ | ------ | ------------------------------------ |
|      |        |        |                                      |

Freeze commit hash: (fill in)

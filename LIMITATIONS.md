# CueScope limitations (v0.1, written before the run; update after results)

1. Text only. CueScope counts manipulative cues in model replies. It does not measure whether any reply changes what a real person believes or does.
2. Small open-weight models only (llama3.2, mistral, llama3). Nothing here says anything about frontier models.
3. Small sample: 30 scenarios and 1 sample per cell. Expect wide confidence intervals and no claim about model rankings.
4. Scenarios were drafted by Claude and then reviewed and edited by the author. They are short, everyday and non-partisan, so they may be easier or less realistic than real conversations. Every scenario states a user leaning, which is why sycophancy can be observed at all.
5. The steering instruction is mild. It asks for persuasion and commitment, not for specific tactics, so it probes a different thing from explicit manipulation prompts.
6. The judges are small open models and can be wrong. Judge A scores everything, judge B only the labelled subset. Agreement with the author's labels is measured on 90 replies and has its own uncertainty.
7. The cue list has 6 cues and is a simplification. Cue boundaries, especially sycophantic_agreement and selective_framing, are subjective.
8. The author is the only human labeller, so there is no human-human agreement estimate.
9. One base seed and one temperature setting.
10. In nearly all scenarios the user leans towards the riskier or more interventionist option, and in the policy scenarios mostly towards supporting the policy. Agreeing with the user is therefore almost always the less balanced reply, and correct agreement is rarely tested. The leaning direction is also confounded with domain, so any domain difference (H2) may partly reflect how the scenarios were written. This was a known design choice made to keep the pilot simple, and results are interpreted with it in mind.
11. Pre-registration is informal: thresholds were committed before the full run but not registered with an external service.

## To add after the run
- Results that contradict or weaken the hypotheses.
- Where the judges failed (cue by cue).
- Parse failure counts and token-cap counts.
- Hardware and timing actually used.
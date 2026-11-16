# CueScope

A small, reproducible evaluation of manipulative cues in open-weight language model replies, with the AI judge validated against human labels.

**Status: Stage 0 and 1 complete (draft). No results yet.**

## What it asks
When an assistant gives advice on finance, health and policy, how often do its replies contain manipulative cues, does a persuasion-steering instruction raise that rate, does an honesty instruction lower it, and can a small LLM judge measure the cues reliably?

## What it does not do
It measures cues in text only. It does not measure effects on people, and it says nothing about frontier models. It is inspired by the propensity side of Akbulut et al. (2026), "Evaluating Language Models for Harmful Manipulation" (arXiv 2603.25326), and is not a replication of it.

## Design
- 30 scenarios (10 finance, 10 health, 10 policy), each with a stated user leaning.
- 3 conditions: neutral, steered (be persuasive and get a commitment), steered_honest (same, plus stay honest and balanced).
- 3 answerers: llama3.2, mistral, llama3. 2 judges: gemma2:9b (all replies) and qwen2.5:14b (hand-labelled subset).
- 6 cues: false urgency, emotional pressure, sycophantic agreement, unwarranted certainty, selective framing, discouraging alternatives.
- 90 replies hand-labelled by the author, blind to model, condition and judge output.
- Hypotheses and thresholds are in `HYPOTHESES.md` and are committed before the full run.

## Repository layout
- `data/scenarios.json`: scenarios (draft, to be verified by the author)
- `prompts/`: condition prompts and the judge prompt
- `rubric/CUES.md`: cue definitions and labelling rules
- `cuescope/`: configuration and validation code
- `tests/`, `scripts/`: structural checks
- `docs/RUN_LOCAL.md`: setup and run commands
- `HYPOTHESES.md`, `LIMITATIONS.md`: analysis plan and limits

## How it was built
The scenarios, prompts, rubric and code were drafted with Claude (Anthropic) and reviewed and edited by the author. (Author: edit this paragraph so it states exactly what you wrote, changed and checked.)

## Hardware
(Fill in after the run: where the models were served, for example "Ollama on a Windows laptop CPU" or "Ollama on a Google Colab T4 GPU".)

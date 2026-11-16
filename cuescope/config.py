"""Central configuration. Standard library only."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENARIOS_PATH = ROOT / "data" / "scenarios.json"
CONDITIONS_PATH = ROOT / "prompts" / "conditions.json"
JUDGE_PROMPT_PATH = ROOT / "prompts" / "judge_prompt.txt"

OLLAMA_URL = "http://localhost:11434"

# Answerers (generate the advice replies).
GENERATORS = ["llama3.2:latest", "mistral:latest", "llama3:latest"]
# Judges. Judge A scores every reply; judge B scores only the hand-labelled subset.
JUDGE_A = "gemma2:9b"
JUDGE_B = "qwen2.5:14b"

CUES = (
    "false_urgency",
    "emotional_pressure",
    "sycophantic_agreement",
    "unwarranted_certainty",
    "selective_framing",
    "discouraging_alternatives",
)
CONDITIONS = ("neutral", "steered", "steered_honest")
DOMAINS = ("finance", "health", "policy")

BASE_SEED = 1601
SAMPLES_PER_CELL = 1
GEN_TEMPERATURE = 0.7
GEN_MAX_TOKENS = 300
JUDGE_TEMPERATURE = 0.0
JUDGE_MAX_TOKENS = 400
N_SCENARIOS = 30
N_HAND_LABELLED = 90  # 10 per (generator, condition) cell


def load_scenarios():
    return json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))["scenarios"]


def load_conditions():
    return json.loads(CONDITIONS_PATH.read_text(encoding="utf-8"))


def build_system_prompt(condition):
    data = load_conditions()
    extra = data["conditions"][condition]
    return (data["base"] + " " + extra).strip()


def render_judge_prompt(scenario, reply):
    """Fill the judge template. Uses replace, not format, because the template contains JSON braces."""
    template = JUDGE_PROMPT_PATH.read_text(encoding="utf-8")
    considerations = "\n".join("- " + c for c in scenario["considerations"])
    return (
        template.replace("{considerations}", considerations)
        .replace("{user_message}", scenario["user_message"])
        .replace("{reply}", reply)
    )


def derive_seed(*parts):
    """Deterministic per-call seed from SHA-256 of the call identity."""
    digest = hashlib.sha256("|".join(str(p) for p in (BASE_SEED,) + parts).encode()).hexdigest()
    return int(digest[:8], 16)


def config_fingerprint():
    """Hash of every setting and prompt that affects results. Stored on each log line later."""
    payload = {
        "generators": GENERATORS,
        "judge_a": JUDGE_A,
        "judge_b": JUDGE_B,
        "base_seed": BASE_SEED,
        "samples": SAMPLES_PER_CELL,
        "gen_temperature": GEN_TEMPERATURE,
        "gen_max_tokens": GEN_MAX_TOKENS,
        "judge_temperature": JUDGE_TEMPERATURE,
        "judge_max_tokens": JUDGE_MAX_TOKENS,
        "conditions": load_conditions(),
        "judge_prompt": JUDGE_PROMPT_PATH.read_text(encoding="utf-8"),
        "scenarios": load_scenarios(),
    }
    blob = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]

import json

from cuescope import config
from cuescope.validate import validate_scenarios


def test_scenarios_structure():
    assert validate_scenarios(config.load_scenarios()) == []


def test_conditions_present_and_differ():
    prompts = {c: config.build_system_prompt(c) for c in config.CONDITIONS}
    assert set(prompts) == set(config.CONDITIONS)
    assert len(set(prompts.values())) == 3
    assert prompts["steered_honest"].startswith(prompts["steered"])


def test_judge_prompt_renders_without_leftover_placeholders():
    s = config.load_scenarios()[0]
    out = config.render_judge_prompt(s, "Example reply text.")
    for token in ("{considerations}", "{user_message}", "{reply}"):
        assert token not in out
    assert s["user_message"] in out and "Example reply text." in out
    for cue in config.CUES:
        assert cue in out


def test_judge_json_example_is_valid_and_has_all_cues():
    text = config.JUDGE_PROMPT_PATH.read_text(encoding="utf-8")
    line = [ln for ln in text.splitlines() if ln.startswith('{"false_urgency"')][0]
    obj = json.loads(line)
    assert tuple(obj) == config.CUES


def test_seed_is_deterministic_and_varies():
    a = config.derive_seed("llama3.2:latest", "F01", "neutral", 0)
    assert a == config.derive_seed("llama3.2:latest", "F01", "neutral", 0)
    assert a != config.derive_seed("llama3.2:latest", "F01", "steered", 0)


def test_fingerprint_stable():
    assert config.config_fingerprint() == config.config_fingerprint()
    assert len(config.config_fingerprint()) == 16


def test_no_em_or_en_dashes_in_project_text():
    skip = {"venv", ".venv", "env", ".git", "__pycache__", ".pytest_cache"}
    for path in config.ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json", ".txt", ".py"}:
            continue
        if skip & set(path.relative_to(config.ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        assert "\u2014" not in text and "\u2013" not in text, str(path)
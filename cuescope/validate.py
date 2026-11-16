"""Structural checks for the scenario file. Content quality still needs the author's review."""
from collections import Counter

from .config import DOMAINS, N_SCENARIOS

REQUIRED = ("id", "domain", "user_message", "considerations")


def validate_scenarios(scenarios):
    problems = []
    if len(scenarios) != N_SCENARIOS:
        problems.append(f"expected {N_SCENARIOS} scenarios, found {len(scenarios)}")
    ids = [s.get("id") for s in scenarios]
    if len(set(ids)) != len(ids):
        problems.append("duplicate scenario ids")
    per_domain = Counter(s.get("domain") for s in scenarios)
    for d in DOMAINS:
        if per_domain.get(d, 0) != N_SCENARIOS // len(DOMAINS):
            problems.append(f"domain {d} has {per_domain.get(d, 0)} scenarios")
    for s in scenarios:
        for key in REQUIRED:
            if key not in s:
                problems.append(f"{s.get('id')}: missing {key}")
        words = len(s.get("user_message", "").split())
        if not 20 <= words <= 80:
            problems.append(f"{s.get('id')}: user_message has {words} words")
        if len(s.get("considerations", [])) != 3:
            problems.append(f"{s.get('id')}: needs exactly 3 considerations")
        for ch in ("\u2014", "\u2013"):
            if ch in s.get("user_message", ""):
                problems.append(f"{s.get('id')}: contains a dash character to remove")
    return problems

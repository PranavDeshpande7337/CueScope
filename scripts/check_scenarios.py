"""Run: python scripts/check_scenarios.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cuescope.config import load_scenarios  # noqa: E402
from cuescope.validate import validate_scenarios  # noqa: E402

scenarios = load_scenarios()
problems = validate_scenarios(scenarios)
print(f"{len(scenarios)} scenarios loaded")
if problems:
    print("PROBLEMS:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("Structure OK. The author must still read every scenario for content.")
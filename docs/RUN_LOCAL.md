# Running CueScope locally (Windows, PowerShell)

## One-off setup
```powershell
cd path\to\CueScope
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# the one model you do not have yet (about 5 GB)
ollama pull gemma2:9b
ollama list
```

## Keep memory under control (15.6 GB RAM)
Set this once, then quit and restart Ollama from the tray icon so it picks it up:
```powershell
setx OLLAMA_MAX_LOADED_MODELS 1
```
Close browsers and other heavy apps before the qwen2.5:14b step.

## Stop the laptop sleeping during long runs
```powershell
powercfg /change standby-timeout-ac 0
powercfg /change monitor-timeout-ac 10
```
Keep it plugged in. Restore your normal sleep timeout afterwards.

## Check Stage 0 and 1
```powershell
python scripts\check_scenarios.py
python -m pytest -q
```

## Quick speed test (used to project full-run time)
```powershell
Measure-Command { ollama run llama3.2 "Give three tips for saving money, in about 150 words." }
Measure-Command { ollama run mistral "Give three tips for saving money, in about 150 words." }
```
Send me both timings along with the model sizes you see in `ollama list`.

## Coming in later stages
Runner, parser, pilot and full-run commands (Stages 3 to 5), the hand-labelling sheet generator (Stage 6) and the analysis script (Stage 7).

# List all available commands
_default:
    @just --list

@bootstrap:
    uv venv
    uv pip install -r requirements.txt

@install:
    uv pip install -r requirements.txt

@serve:
    uv run sphinx-autobuild . _build/html --port 8002
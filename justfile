# List all available commands
_default:
    @just --list

@bootstrap:
    uv venv
    uv pip install -r requirements.txt

@install:
    uv pip install -r requirements.txt

@serve PORT="8002":
    uv run sphinx-autobuild . _build/html --port {{ PORT }}
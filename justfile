dev:
    uv run maturin develop

check:
    cargo fmt -- --check && cargo check && uv run ruff check . && uv run ruff format --check . && uv run pytest -q

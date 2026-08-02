coverage:
    uv run coverage run --source=py-page -m pytest
    uv run coverage report -m
    uv run coverage xml
    uv run genbadge coverage -i coverage.xml
    rm coverage.xml

doc:
    uv run zensical serve

test:
    uv run pytest

clean:
    rm -rf __pycache__ .pytest_cache

flake:
    flake8 common.py tests.py

check: flake test clean

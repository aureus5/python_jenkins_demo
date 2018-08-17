#!/usr/bin/env bash

python -m pytest test/test_move9.py

python -m pytest test/test_lru_cache.py

python -m pytest test/test_lru_cache_corner.py

python -m pytest test/test_performance.py
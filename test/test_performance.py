import pytest
import time
import numpy as np
from src.lru_cache import LRUCache
from src.lru_cache_big_O_n import LRUCacheOn


# Test cases
cache_capacity_test_cases = [
    10,
    100,
    1000,
    2000
]


@pytest.mark.parametrize("cap", cache_capacity_test_cases)
def test_many_set_op_util(cap):
    capacity = cap
    cache = LRUCache(capacity)
    cache_on = LRUCacheOn(capacity)

    cache_time = np.array(get_exec_time(cache, 5, capacity))
    cache_on_time = np.array(get_exec_time(cache_on, 5, capacity))
    print("")
    print("using cache, capacity=", capacity, "average exec=", np.mean(cache_time), "standad dev=", np.std(cache_time))
    print("using cache, capacity=", capacity, "average exec=", np.mean(cache_on_time), "standad dev=", np.std(cache_on_time))


def get_exec_time(_cache, repeat, capacity):
    time_list = []
    for i in range(repeat):
        cache_time_start = time.time()
        for j in range(capacity):
            _cache.set(j, j + 1)
        for k in range(capacity, capacity * 2):
            _cache.set(k, k + 10)
        time_list.append(time.time() - cache_time_start)
    return time_list

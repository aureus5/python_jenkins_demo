import pytest
from src.lru_cache import LRUCache

# capacity is zero
def test_capacity_empty():
    cache = LRUCache(0)
    assert cache.capacity == 0


def test_capacity_empty_set():
    cache = LRUCache(0)
    assert cache.capacity == 0
    cache.set(3, 5)     # detect a bug
    assert cache.capacity == 0


def test_capacity_empty_set2():
    cache = LRUCache(0)
    assert cache.capacity == 0
    for i in range(100):
        cache.set(i, i+1)
    assert cache.capacity == 0


def test_capacity_empty_get():
    cache = LRUCache(0)
    assert cache.capacity == 0
    assert cache.get(3) == -1


def test_capacity_empty_get2():
    cache = LRUCache(0)
    assert cache.capacity == 0
    cache.set(3, 33)
    assert cache.get(3) == -1


def test_capacity_empty_get3():
    cache = LRUCache(0)
    assert cache.capacity == 0
    for i in range(100):
        cache.set(i, i+1)
    for i in range(100):
        cache.get(i)
    assert cache.capacity == 0
    assert cache.get(3) == -1

# capacity is max int(2,147,483,647)
def test_capacity_max_int():
    limit = pow(2, 31) - 1
    cache = LRUCache(limit)
    assert cache.capacity == pow(2, 31) - 1


def test_capacity_max_int_op():
    limit = pow(2, 31) - 1
    cache = LRUCache(limit)
    for i in range(1000, 2000):
        cache.set(i, i / 2 + 3)
    for j in range(1500, 2500):
        cache.get(j)
    assert cache.capacity == pow(2, 31) - 1
    assert cache.get(1010) == 508


# capacity is negative number
def test_capacity_neg():
    with pytest.raises(ValueError):       # detect a bug
        assert LRUCache(-1)


def test_capacity_neg2():
    with pytest.raises(ValueError):
        assert LRUCache(-3)


def test_capacity_neg3():
    cache_size = -pow(2, 31)
    with pytest.raises(ValueError):
        assert LRUCache(cache_size)
import pytest
from src.lru_cache import LRUCache


def test_add_capacity_changes_empty():
    cache = LRUCache(0)
    assert cache.capacity == 0


def test_add_capacity_changes_n():
    cache = LRUCache(5)
    assert cache.capacity == 5
    cache.set(3, 5)
    assert cache.capacity == 5


def test_add_capacity_limit():
    cache = LRUCache(3)
    assert cache.capacity == 3
    cache.set(3, 5)
    cache.set(2, 6)
    cache.set(1, 7)
    cache.set(0, 8)
    cache.set(11, 12)
    cache.set(13, 14)
    cache.set(15, 16)
    assert cache.capacity == 3


def test_add_capacity_override():
    cache = LRUCache(4)
    assert cache.capacity == 4
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    cache.set(3, 3)
    assert cache.capacity == 4


def test_get_key_exist():
    cache = LRUCache(3)
    cache.set(3, 335)
    assert cache.get(3) == 335


def test_get_key_not_exist():
    cache = LRUCache(3)
    cache.set(3, 335)
    assert cache.get(4) == -1


def test_least_recent_evicted():
    cache = LRUCache(3)
    cache.set(2, 12)
    cache.set(4, 14)
    cache.set(5, 15)   # key=2 is LRU
    assert cache.get(4) == 14  # key=2 is LRU
    cache.set(7, 17)           # key=2 is evicted
    assert cache.get(2) == -1
    assert cache.get(4) == 14


def test_least_recent_changed_then_evicted():
    cache = LRUCache(3)
    cache.set(2, 12)
    cache.set(4, 14)
    cache.set(5, 15)   # key=2 is LRU
    assert cache.get(2) == 12  # key=4 is LRU
    cache.set(7, 17)           # key=4 is evicted
    assert cache.get(2) == 12
    assert cache.get(4) == -1


def test_long_sequence():
    cache = LRUCache(3)
    cache.set(2, 22)
    cache.set(1, 11)
    cache.set(5, 55)
    assert cache.get(3) == -1
    cache.set(7, 77)
    assert cache.get(2) == -1
    assert cache.get(7) == 77
    cache.set(8, 88)
    assert cache.get(1) == -1
    assert cache.get(5) == 55
    cache.set(8, -88)
    assert cache.get(5) == 55
    assert cache.get(8) == -88

def test_longer_sequence():
    cache = LRUCache(100)
    for i in range(1,101):
        cache.set(i, i+100)
    assert cache.capacity == 100
    assert cache.get(100) == 200
    cache.set(101, 201)
    cache.set(102, 202)
    assert cache.get(1) == -1
    assert cache.get(2) == -1
    assert cache.get(3) == 103


def test_longer_sequence2():
    limit = pow(2,10)
    cache = LRUCache(limit)
    for i in range(1,limit+1):
        cache.set(i, i+100)
    assert cache.capacity == limit
    assert cache.get(100000) == -1
    cache.set(10100, -201)
    cache.set(10200, -202)
    assert cache.get(10100) == -201
    assert cache.get(1) == -1
    assert cache.get(2) == -1
    assert cache.get(3) == 103
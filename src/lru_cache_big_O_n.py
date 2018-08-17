

'''
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.set(1, 1);
cache.set(2, 2);
cache.get(1);       // returns 1
cache.set(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.set(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
import sys

class Node(object):
    def __init__(self, key, value, index):
        self.key = key
        self.val = value
        self.index = index


class LRUCacheOn(object):
    def __init__(self, capacity):
        if capacity < 0:    # bug found: capacity should not be negative number
            raise ValueError("capacity has to be equal or greater than 0")
        self.capacity = capacity
        self.dict = dict()
        self.index = 0

    def get(self, key):
        if key in self.dict:
            this_node = self.dict[key]
            this_node.index = self.index
            self.index += 1
            return this_node.val
        return -1

    def set(self, key, value):
        if key in self.dict:
            new_n = Node(key, value, self.index)
            self.index += 1
            self.dict[key] = new_n
        else:
            new_n = Node(key, value, self.index)
            self.index += 1
            if len(self.dict) >= self.capacity:
                if self.capacity <= 0:        # bug found: if capacity is zero, set operation should not pop elements
                    return
                self.evict_lru()
                self.dict[key] = new_n
            self.dict[key] = new_n

    def evict_lru(self):
        lru_index = sys.maxsize
        lru_key = -1
        for key in self.dict:
            if lru_index > self.dict[key].index:
                lru_index = self.dict[key].index
                lru_key = key
        self.dict.pop(lru_key, None)


def print_dict(d):
    for k in d:
        print(k, d[k].val)


if __name__ == '__main__':
    cache = LRUCacheOn(3)
    cache.set(4, 14)
    cache.set(2, 12)
    cache.set(5, 15)
    cache.get(4)
    print_dict(cache.dict)
    print("")
    cache.set(7, 17)
    print_dict(cache.dict)
    print("")

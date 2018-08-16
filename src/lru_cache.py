

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


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        if capacity < 0:    # bug found: capacity should not be negative number
            raise ValueError("capacity has to be equal or greater than 0")
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = dict()

    def get(self, key):
        if key in self.dict:
            moving_node = self.dict[key]
            self.remove_from_list(moving_node)
            self.add_to_list(moving_node)
            return moving_node.val
        return -1

    def set(self, key, value):
        new_n = Node(key, value)
        if key in self.dict:
            self.remove_from_list(self.dict[key])
            self.add_to_list(new_n)
            self.dict[key] = new_n
        else:
            if len(self.dict) >= self.capacity:
                # if self.capacity <= 0:        # bug found: if capacity is zero, set operation should not pop elements
                #     return
                remove_n = self.tail.pre
                self.dict.pop(remove_n.key, None)
                self.remove_from_list(remove_n)
            self.add_to_list(new_n)
            self.dict[key] = new_n

    def remove_from_list(self, moving_node):
        pre_n = moving_node.pre
        next_n = moving_node.next
        pre_n.next = next_n
        next_n.pre = pre_n

    def add_to_list(self, moving_node):
        first_n = self.head.next
        self.head.next = moving_node
        moving_node.pre = self.head
        moving_node.next = first_n
        first_n.pre = moving_node


def print_dict(d):
    for k in d:
        print(k, d[k].val)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set(4, 14)
    cache.set(2, 12)
    cache.set(5, 15)
    cache.get(4)
    print_dict(cache.dict)
    print("")
    cache.set(7, 17)
    print_dict(cache.dict)
    print("")

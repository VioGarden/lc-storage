from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None) # node after the tail node
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        # adds to head
        node.next = self._sentinel.next # points to same as sentinel point
        node.prev = self._sentinel # prev poined to sentinel
        node.next.prev = node # backwards pointer (Double linked)
        self._sentinel.next = node # sentinel pointed to node
        self._size += 1 # size update
    
    def pop(self, node=None):
        if self._size == 0:
            return
        if not node:
            node = self._sentinel.prev # if no args, tail node is removed
        # pointers set for prev and next nodes
        node.prev.next = node.next # prev pointer moved from curr node to next
        node.next.prev = node.prev # prev pointer of next node moved to prev of curr
        self._size -= 1
        return node # return removed node

class LFUCache(object):

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._node = dict() # hashmap to every node (for O(1) retrieval)
        self._freq = defaultdict(DLinkedList) 
        self._minfreq = 0

    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node) # .pop is a method in DLL
        if self._minfreq == freq and not self._freq[freq]:
            # if node was last in the smallest freq DLL, _minfreq += 1
            self._minfreq += 1
        node.freq += 1 # new frequency (for every node update)
        freq = node.freq
        self._freq[freq].append(node) # .append is method in DLL

    def get(self, key):
        if key not in self._node:
            return -1
        node = self._node[key]  # get node
        self._update(node) # update node (with helper function)
        return node.val # return the value

    def put(self, key, value):
        if self._capacity == 0:
            return
        if key in self._node:
            # if already an existing key do same thing as get and update value
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                # _freq --> DLL; _minfreq --> Smallest DLL
                node = self._freq[self._minfreq].pop() # remove least frequent
                del self._node[node.key] # delete from {key: node} hashmap
                self._size -= 1 # size -= 1
            node = Node(key, value) # create new node
            self._node[key] = node # hashmap is {key : node}
            self._freq[1].append(node) # create new DLL and append node
            self._minfreq = 1 # reset minfreq to 1
            self._size += 1 # size += 1

    # Things learned: 
    # _sentinel node  (.prev and .next)
    # collections.defaultdict(DoublyLinkedList) // class hashmap
    # self._freq[1].append(node) // create hashmap
    # DLL pop and append helper functions
    # LFU _update helper function
    # ._minfreq (to help keep track of lowest freq DLL)
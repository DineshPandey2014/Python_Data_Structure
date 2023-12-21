"""
https://leetcode.com/problems/design-hashmap/description/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

"""

class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

"""
Hasmap implementation is of array od list
means you have [ListNode(), ListNode(), ...]
"""
class MyHashMap:

    def __init__(self):
        # It creates a lis of thousand node. Means initally we initalize a map of 1000 nodes.
        # After that it get rehash
        self.map = [ListNode() for i in range(1000)]

    # Hash function which gives the hashcode.
    def hash(self, key):
        return key % len(self.map)

    # First take a key and map to index with HashFunction
    # Handle two case.
    # Case :1 If key is not present in the map
    # Case :2 If key is present in map. Override the value
    def put(self, key: int, value: int) -> None:
        hash_key = self.hash(key)
        curr = self.map[hash_key] # It point the dummy node
        while curr.next:
            # Case when the key already exist. It overrides the value
            if curr.next.key == key:
                curr.next.val = value
                return
        #This is the case when curr.next is None. It reachd to the last node of linked list
        # Couldn't find the key.
        # This the case when we insert first key and value to Hashmap
        curr.next = ListNode(key, value)

    # Get the head of the key
    def get(self, key: int) -> int:
        hash_key = self.hash(key)
        #curr = self.map[hash_key] # This is the dummy node
        curr = self.map[hash_key].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key):
        hash_key = self.map(key)
        curr = map[hash_key] # Get the dummy node
        # Either will reach to end of the loop will not remove
        # Will remove once we found the mathicng key
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next







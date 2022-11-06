"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

- MyHashMap() initializes the object with an empty map.

- put(key, value) inserts a (key, value) pair into the HashMap. If the key already exists in the map,
update the corresponding value.

- get(key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.

- remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.hash_table = [None] * self.capacity

    def hash(self, key):
        index = key % self.capacity
        return index

    def put(self, key, value):
        index = self.hash(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = Node(key, value)

        else:
            curr_node = self.hash_table[index]
            while curr_node:
                if curr_node.key == key:
                    curr_node.value = value
                    return
                if curr_node.next is None:
                    break
                curr_node = curr_node.next
            curr_node.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)

        curr_node = self.hash_table[index]

        while curr_node:
            if curr_node.key == key:
                return curr_node.value
            curr_node = curr_node.next
        return -1

    def remove(self, key):
        index = self.hash(key)

        if self.hash_table[index] is None:
            return

        curr_node = prev_node = self.hash_table[index]
        if curr_node.key == key:
            self.hash_table[index] = curr_node.next
        else:
            curr_node = curr_node.next

            while curr_node:
                if curr_node.key == key:
                    prev_node.next = curr_node.next
                    break
                else:
                    prev_node = prev_node.next
                    curr_node = curr_node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
An implementation of hash table with collision resolution by chaining (with minimal required LinkedList implementation
based on lists)
Hash function is designed as a hash for integers, operations of adding items and searching for items are implemented
"""


def calculate_hash(data: int):
    """
    A polynomial hash-function that returns a 32-bit hash
    :param data: data
    :return:
    """
    k = 3571
    s = 0
    i = 1
    data += 84832941

    while data > 0:
        s += data % 2 * k ** i
        i += 1
        data //= 2
    return s % 2 ** 32


class LinkedList:
    """
    LinkedList implementation based on lists, minimal functionality required for Hash Table implementation
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        """
        Method adds item to a LinkedList
        :param item: added item
        :return:
        """
        if not self.search(item):
            node = [item, None]
            if self.head is None:
                self.head = node
            else:
                self.tail[1] = node
            self.tail = node

    def search(self, item):
        """
        method searches LinkedList for an item
        :param item: item searched
        :return: bool
        """
        curr = self.head
        while curr is not None:
            if curr[0] == item:
                return True
            curr = curr[1]
        return False


class HashTable:
    def __init__(self):
        self.table = [LinkedList() for _ in range(256)]

    def add(self, item):
        """
        Method adds item to a HashTable
        :param item: added item
        :return:
        """
        hsh = calculate_hash(item)
        if hsh > len(self.table):
            hsh = hsh % len(self.table)
        self.table[hsh].add(item)

    def search(self, item):
        """
        method searches HashTable for an item
        :param item: item searched
        :return: bool

        """
        hsh = calculate_hash(item)
        if hsh > len(self.table):
            hsh = hsh % len(self.table)
        return self.table[hsh].search(item)


if __name__ == '__main__':
    h_table = HashTable()

    h_table.add(445103176)
    h_table.add(292103050)
    h_table.add(445104176)
    h_table.add(292102050)
    h_table.add(445105176)
    h_table.add(292101050)
    h_table.add(445203176)
    h_table.add(292403050)

    print(h_table.search(445103176))
    print(h_table.search(292103051))

    for llist in h_table.table:
        if llist.head is not None:
            print(llist.head)


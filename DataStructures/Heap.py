"""Heap is a special binary tree structure.
If each parent node is less than or equal to its child node it is called a Min Heap.
If each parent node is greater than or equal to its child node then it is called a Max Heap.
NB! If implemented using an array or list, child nodes of node with index [i] have indexes [2 * i + 1] and [2 * i + 2];
parent node of node with index [i] has index [(i - 1) // 2]
"""


class Heap:  # Min Heap implementation
    def __init__(self):
        """
        Using a list to implement heap structure
        """
        self.values = []
        self.size = 0

    def lift_item(self, i):
        """
        Method is used to lift item in heap structure if its value is less than its parent item value
        :param i: index of item
        :return:
        """
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:  # (i - 1) // 2 is parent index for item index i
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def insert(self, value):
        """
        Method is used add an item to heap and rearrange heap after that
        :param value: a given value
        :return:
        """
        self.values.append(value)
        self.size += 1
        self.lift_item(self.size - 1)

    def lower_item(self, i):
        """
        Method is used to lower item in heap structure if its value is less than its parent item value
        :param i: index of item
        :return:
        """
        while 2 * i + 1 < self.size:  # checking that heap node has at least 1 child
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if j == i:
                break
            else:
                self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def extract_min(self):
        """
        Method is used to remove the item with the lowest value in heap and rearrange heap after that
        :return: lowest value item
        """
        if not self.size:
            return None
        popped_data = self.values[0]
        self.values[0] = self.values[-1]  # last item is put on top to preserve heap structure
        self.values.pop()
        self.size -= 1
        self.lower_item(0)  # searching for fitting place for item that used to be last
        return popped_data


def heapify(array):
    """
    Converts array to Heap with O(n log n) complexity
    :param array: given array
    :return: Heap object
    """
    heap = Heap()
    for item in array:
        heap.insert(item)
    return heap


def heapify_fast(array):
    """
    Converts array to Heap with O(n) complexity
    :param array: given array
    :return: Heap object
    """
    heap = Heap()
    heap.values = array[:]
    heap.size = len(array)
    for i in reversed(range(heap.size // 2)):
        heap.lower_item(i)
    return heap


if __name__ == '__main__':
    test_array = [46, 15, 3, 4, 21, 79, 61]

    test_heap = heapify_fast(test_array)

    print(test_heap.values)

    test_heap.insert(1)
    print(test_heap.values)

    for _ in range(test_heap.size + 1):
        tmp = test_heap.extract_min()
        print(tmp)
    print(test_heap.values)


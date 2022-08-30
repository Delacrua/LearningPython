"""
Implementation of binary search of a certain key value in a sorted array with a O(log n) complexity.
left_bound by default is -1 and shows position in array previous to the first instance of key value we are
searching for
right_bound by default equals to len(array) and shows position next to the last instance of key value we are
searching for
"""


def binary_search(array: list, key):
    """
    The function find left and right bounds of given key value in array and returns them in form of tuple
    :param array: given array
    :param key: key value to search
    :return: a tuple of following structure: (position in array previous to the first instance of key value,
    position in array next to the last instance of key value) or None if no key_value found in array
    """

    def _find_left_bound(collection, key_value) -> int:
        """
        The function finds position in collection previous to the first instance of key value
        :param collection: given collection
        :param key_value: value to search
        :return:
        """
        left = - 1
        right = len(collection)
        while right - left > 1:
            middle = (left + right) // 2
            if array[middle] < key_value:
                left = middle
            else:
                right = middle
        return left

    def _find_right_bound(collection, key_value) -> int:
        """
        The function finds position in collection next to the last instance of key value
        :param collection: given collection
        :param key_value: value to search
        :return:
        """
        left = - 1
        right = len(collection)
        while right - left > 1:
            middle = (left + right) // 2
            if array[middle] <= key_value:
                left = middle
            else:
                right = middle
        return right

    left_boundary = _find_left_bound(array, key)
    right_boundary = _find_right_bound(array, key)
    return None if right_boundary - left_boundary == 1 else (left_boundary, right_boundary)


test_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]
print(binary_search(test_list, 5))

test_list = [1, 2, 3, 4, 4, 6, 6, 7, 8]
print(binary_search(test_list, 5))

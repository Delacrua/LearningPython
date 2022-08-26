"""
This sorting algorithm has time complexity of O(n*log n)
1. Divide and conquer algorithm
2. Requires additional memory to operate (creation of sub-lists and resulting list)
3. Can be implemented both as stable and unstable algorithm
Base idea is in recurrent splitting of a collection into single elements and then merging them back while sorting
"""


def merge_lists(left: list, right: list) -> list:
    """
    The function merges two sorted lists into a new sorted list, that contains items of both lists combined
    in sorted order
    :param left: first sorted list
    :param right: second sorted list
    :return: a sorted list
    """
    result = []
    i, j = 0, 0  # i and j are pointers to positions in lists we are merging
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= for sorting to be stable, make it < to make sorting unstable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(unsorted_list: list) -> list:
    """
    The function takes an unsorted list as an argument and returns a sorted list using a recurrent algorithm
    :param unsorted_list: an unsorted list
    :return: a sorted list
    """
    if len(unsorted_list) < 2:
        return unsorted_list[:]
    else:
        middle = len(unsorted_list) // 2
        left_half = unsorted_list[:middle]
        right_half = unsorted_list[middle:]
        return merge_lists(merge_sort(left_half), merge_sort(right_half))


test_list = [1, 5, 3, 2, 7, 8, 4, 9, 6, 14, 12]

print(merge_sort(test_list))

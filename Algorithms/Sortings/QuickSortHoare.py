"""
This sorting algorithm has time complexity of O(n*log n) but in corner cases (sorted or almost sorted list)
can be slower up to O(n^2)
1. Divide and conquer algorithm
2. Can be implemented as In place algorithm, (doesn't create additional sub-lists (still requires some memory for
function call stack))
3. Can be implemented as a Stable or Unstable algorithm
Base idea is in recurrent splitting of a collection into parts of elements that are less than, equal to, or greater than
some chosen border element (pivot)
"""


def quicksort(unsorted_list: list) -> list:
    """
    The function takes an unsorted list as an argument and returns a sorted list using a recurrent algorithm
    (not an In place implementation, but a Stable one)
    :param unsorted_list: an unsorted list
    :return: a sorted list
    """
    if unsorted_list:
        pivot = unsorted_list[0]
        left = [i for i in unsorted_list[1:] if i < pivot]  # left for less than pivot
        middle = unsorted_list[0:1] + [i for i in unsorted_list[1:] if i == pivot]  # middle for equal to pivot
        right = [i for i in unsorted_list[1:] if i > pivot]  # right for greater than pivot
        return quicksort(left) + middle + quicksort(right)
    else:
        return unsorted_list


def quicksort_in_place(given_list):
    """
    The function takes an unsorted list as an argument and returns a sorted list using a recurrent algorithm
    and Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort
    :param given_list: an unsorted list
    :return: a sorted list
    """
    def _quicksort(given_list, left, right):
        # must run partition on sections with 2 elements or more
        if left < right:
            splitter = partition(given_list, left, right)
            _quicksort(given_list, left, splitter)
            _quicksort(given_list, splitter + 1, right)

    def partition(given_list, left, right):
        pivot = given_list[left]
        while True:
            while given_list[left] < pivot:
                left += 1
            while given_list[right] > pivot:
                right -= 1
            if left >= right:
                return right
            given_list[left], given_list[right] = given_list[right], given_list[left]
            left += 1
            right -= 1

    _quicksort(given_list, 0, len(given_list)-1)
    return given_list


example1 = [4, 5, 1, 2, 3]
exp_result1 = [1, 2, 3, 4, 5]
res1 = quicksort(example1)
res1_2 = quicksort_in_place(example1)
print(res1, res1 == exp_result1)
print(res1_2, res1_2 == exp_result1)

example2 = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8, 2]
exp_result2 = [1, 2, 2, 2, 4, 4, 5, 6, 6, 7, 8]
res2 = quicksort(example2)
res2_2 = quicksort_in_place(example2)
print(res2, res2 == exp_result2)
print(res2_2, res2_2 == exp_result2)

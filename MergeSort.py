def merge(left, right):
    """
    The function merges sorted two sorted arrays into a new sorted array, that contains items of both arrays combined
    in sorted order
    :param left: first sorted array
    :param right: second sorted array
    :return: a sorted array
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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

def merge_sort(list):
    if len(list) < 2:
        return list[:]
    else:
        n = len(list) // 2
        left_half = list[:n]
        right_half = list[n:]
        return merge(merge_sort(left_half), merge_sort(right_half))

a = [1, 5, 3, 2 ,7, 8, 4, 9, 6, 14, 12]

print(merge_sort(a))
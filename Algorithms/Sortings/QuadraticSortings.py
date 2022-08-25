def insert_sort(unsorted_list: list):
    """ sorts the list using insert mechanism"""
    for i in range(len(unsorted_list) - 1):
        cur_pos = i + 1
        for j in range(i + 1):
            if cur_pos > 0 and unsorted_list[cur_pos] < unsorted_list[cur_pos - 1]:
                unsorted_list[cur_pos], unsorted_list[cur_pos - 1] = unsorted_list[cur_pos - 1], unsorted_list[cur_pos]
                cur_pos -= 1


a = [3, 1, 2, 6, 5, 4]

print('Insert sort')
print(a)
insert_sort(a)
print(a)


def choice_sort(unsorted_list: list):
    """ sorts the list using choice mechanism"""
    for i in range(len(unsorted_list) - 1):
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[i]:
                unsorted_list[j], unsorted_list[i] = unsorted_list[i], unsorted_list[j]


a = [3, 1, 2, 6, 5, 4]

print("Choice sort")
print(a)
choice_sort(a)
print(a)


def bubble_sort(unsorted_list: list):
    """ sorts the list using bubble mechanism with break during cycle if list already sorted"""
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - 1 - i):
            flag = True
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                flag = False
        if flag:
            print("Finished on iteration №", i + 1)
            break


a = [3, 1, 2, 6, 5, 4]

print("Bubble sort")
print(a)
bubble_sort(a)
print(a)

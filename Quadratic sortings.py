def insert_sort(unsorted_list:list):
    """ sorts the list using insert mechanism"""
    for i in range(len(unsorted_list)-1):
        current_position = i + 1
        for j in range(i+1):
            if current_position > 0 and unsorted_list[current_position] < unsorted_list[current_position - 1]:
                unsorted_list[current_position], unsorted_list[current_position - 1] = unsorted_list[current_position - 1], unsorted_list[current_position]
                current_position -= 1

a = [3, 1, 2, 6, 5, 4]

print('Сортировка вставками')
print(a)
insert_sort(a)
print(a)


def choice_sort(unsorted_list:list):
    """ sorts the list using choise mechanism"""
    for i in range(len(unsorted_list)-1):
        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[i]:
                unsorted_list[j], unsorted_list[i] = unsorted_list[i], unsorted_list[j]


a = [3, 1, 2, 6, 5, 4]

print("сортировка выбором")
print(a)
choice_sort(a)
print(a)



def bubble_sort(unsorted_list:list):
    """ sorts the list using bubble mechanism"""
    for i in range(len(unsorted_list)-1):
         for j in range(len(unsorted_list)-1-i):
             flag = True
             if unsorted_list[j] > unsorted_list[j+1]:
                 unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j+1], unsorted_list[j]
                 flag = False
         if flag:
             print("Завершена на итерации №", i + 1)
             break



a = [3, 1, 2, 6, 5, 4]

print("Сортировка пузырьком")
print(a)
bubble_sort(a)
print(a)
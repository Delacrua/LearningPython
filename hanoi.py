def hanoi(n, i, k):
    '''
    The function visualizes the way to solve Hanoi Tower puzzle for 3 rods and n disks using recursion algorithm
    :param n: number of disks on the first rod
    :param i: the number of the stift where the original tower stands
    :param k: the number of the disk, where tower must be moved
    :return: None

    '''
    if n == 1:
        print(f"Переложи диск 1 с стержня {i} на стержень {k}")
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(f"Переложи диск {n} с стержня {i} на стержень {k}")
        hanoi(n-1, tmp, k)


hanoi(4, 1, 2)
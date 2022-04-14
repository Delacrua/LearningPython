def hanoi(n, i, k):
    '''
    The function prints order of operations to solve Hanoi Tower puzzle for 3 rods and n disks using recursion algorithm
    :param n: number of disks on the starting rod
    :param i: the number of the rod on which the original tower stands
    :param k: the number of the rod to which the tower must be moved
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
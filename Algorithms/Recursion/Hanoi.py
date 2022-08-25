def solve_hanoi(n, i, k):
    """
    The function prints order of operations to solve Hanoi Tower puzzle for 3 Rods and n Disks using recurrent algorithm
    :param n: number of Disks on the starting Rod
    :param i: the number of the Rod on which the original tower stands
    :param k: the number of the Rod to which the tower must be moved
    :return: None
    """
    if n == 1:
        print(f"Move Disk 1 from Rod {i} to Rod {k}")
    else:
        tmp = 6 - i - k
        solve_hanoi(n - 1, i, tmp)
        print(f"Move Disk {n} from Rod {i} to Rod {k}")
        solve_hanoi(n - 1, tmp, k)


solve_hanoi(4, 1, 2)

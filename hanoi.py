def hanoi(n, i, k):
    if n == 1:
        print(f"Переложи диск 1 с стержня {i} на стержень {k}")
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(f"Переложи диск {n} с стержня {i} на стержень {k}")
        hanoi(n-1, tmp, k)


hanoi(4, 1, 2)
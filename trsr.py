def array_diff(a, b):
    s = ' '.join([str(i) for i in a])
    for i in ''.join([str(i) for i in b]):
        s.replace(i, '')
    return [int(i) for i in s.split()]

array_diff([1,2,2], [1])
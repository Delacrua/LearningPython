def generator():
    counter = 0
    while counter < 10:
        new_value = yield counter
        if new_value is not None:
            counter = new_value
        else:
            counter += 1



if __name__ == '__main__':
    g = generator()

    print(g.gi_frame.f_locals)

    print(next(g))
    print(g.gi_frame.f_locals)

    print(next(g))
    print(g.gi_frame.f_locals)

    g.send(7)
    print(g.gi_frame.f_locals)

    try:
        g.send(10)
    except StopIteration:
        print('StopIteration')

    assert g.gi_running is False

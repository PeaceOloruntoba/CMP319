import math as mt


def heuns_method(func, init_value_y, init_value_x, h, N):
    count = 0

    while count != N:
        k1 = func(x=init_value_x, y=init_value_y)
        k2 = func(x=init_value_x + (2 * h) / 3, y=init_value_y + (2 * k1 * h) / 3)

        next_value_of_yn = init_value_y + (h / 4) * (k1 + 3 * k2)
        print("\n")
        next_value_of_xn = init_value_x + h
        print(next_value_of_xn)

        init_value_y = next_value_of_yn
        init_value_x = next_value_of_xn
        count += 1

Q = lambda x, y: 3 * (x ** 2) * y

heuns_method(Q, 0, 0, 0.1, 10)
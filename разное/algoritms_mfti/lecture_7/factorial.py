def f(n: int):
    assert n >= 0, "Факториал отрицательного не определён"
    if n == 0:
        return 1
    return f(n-1) * n


if __name__ == '__main__':
    print(f(4))
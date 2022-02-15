def pow(a: float, n: int) -> float:
    if n == 0:
        return 1
    return pow(a, n - 1) * a


def pow_fast(a: float, n: int) -> float:
    if n == 0:
        return 1
    elif n % 2 == 1:
        pow(a, n - 1) * a
    else:
        return pow(a * a, n // 2)

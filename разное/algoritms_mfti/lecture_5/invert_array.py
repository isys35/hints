def invert_array(A: list, N: int):
    """Обращение массива (поворрот задом-наперёд)
    в рамках индексов от 0 до N-1"""
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok ")
    else:
        print("#test1 - fail")

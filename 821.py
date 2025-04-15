import math

def a_n(x: float, n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    a = 1

    yield a
    for i in range(1, n+1):
        a *= x / i
        yield a

def harmonic_series(max_n: int | None = None):
    n = 1
    if max_n is None:
        max_n = float('inf')
    while n <= max_n:
        yield 1 / n
        n += 1

def harmonic_series_sum(max_n: int | None = None):
    s = 0
    for i in harmonic_series(max_n):
        s += i
        yield s


def det(A: list[list[float]]) -> float:
    ...

def P_n(max_n: int | None = None):
    a_prev_3 = 1
    a_prev_2 = 1
    a_prev_1 = 3
    
    p = 1
    yield p
    
    p *= a_prev_2 / 3
    yield p
    
    p *= a_prev_1 / 3**2
    yield p
    
    n = 3
    if max_n is None:
        max_n = float('inf')
    
    while n <= max_n:
        a_current = a_prev_3 + (4*n-2)/(2*n-1)
        
        p *= a_current / (3**n)
        yield p
        
        a_prev_3, a_prev_2, a_prev_1 = a_prev_2, a_prev_1, a_current
        n += 1


def taylor_exp(x: float, epsilon: float = 1e-10) -> tuple[float, int]:
    result = 1.0
    term = 1.0
    i = 1
    
    while abs(term) >= epsilon:
        term *= x / i
        result += term
        i += 1
    
    return result, i-1

def compare_with_library(function_name: str, taylor_func, lib_func, x: float, epsilon: float = 1e-10) -> None:
    taylor_value, terms = taylor_func(x, epsilon)
    lib_value = lib_func(x)
    abs_error = abs(taylor_value - lib_value)
    rel_error = abs_error / abs(lib_value) if lib_value != 0 else abs_error
    
    print(f"\n{function_name}({x}) comparison:")
    print(f"Taylor series (used {terms} terms): {taylor_value}")
    print(f"Library math: {lib_value}")
    print(f"Absolute error: {abs_error}")
    print(f"Relative error: {rel_error}")
    print(f"Precision ε reached: {abs_error < epsilon}")

def taylor_series_examples():
    test_values = [0, 0.5, 1, 2, 5, 10]
    epsilon = 1e-10
    
    for x in test_values:
        compare_with_library("exp", taylor_exp, math.exp, x, epsilon)


def matrix_det(max_n: int | None = None):
    """
    Calculate the determinant of a matrix of rank n.
    Matrix: 
    D_n = [
        [5, 3, 0, 0, ..., 0, 0, 0],
        [2, 5, 3, 0, ..., 0, 0, 0],
        [0, 2, 5, 3, ..., 0, 0, 0],
        [0, 0, 2, 5, ..., 0, 0, 0],
        ...,
        [0, 0, 0, 0, ..., 2, 5, 3],
        [0, 0, 0, 0, ..., 0, 2, 5]
    ]
    
    Args:
        n: rank of the matrix
    """
    d_n_1, d_n_2 = 19, 5
    yield d_n_2
    yield d_n_1

    n = 2
    if max_n is None:
        max_n = float('inf')
    
    while n <= max_n:
        d_n = 5 * d_n_1 - 6 * d_n_2
        yield d_n
        d_n_2, d_n_1 = d_n_1, d_n
        n += 1

for i in matrix_det(None):
    print(i)


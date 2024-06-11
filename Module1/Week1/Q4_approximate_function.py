import math


def approx_sin(x, n):
    result = sum((-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1) for i in range(n))
    return result


def approx_cos(x, n):
    result = sum((-1) ** i * x ** (2 * i) / math.factorial(2 * i) for i in range(n))
    return result


def approx_sinh(x, n):
    result = sum(x ** (2 * i + 1) / math.factorial(2 * i + 1) for i in range(n))
    return result


def approx_cosh(x, n):
    result = sum(x ** (2 * i) / math.factorial(2 * i) for i in range(n))
    return result


print(approx_sin(3.14, 10))
print(approx_cos(3.14, 10))
print(approx_sinh(3.14, 10))
print(approx_cosh(3.14, 10))

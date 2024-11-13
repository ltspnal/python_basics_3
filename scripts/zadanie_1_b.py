import math


def taylor_cos(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        result += term
    return result


x = math.radians(60)
approx_cos = taylor_cos(x, terms=10)
exact_cos = math.cos(x)

print(f"Приближённое значение cos(60°): {approx_cos}")
print(f"Точное значение cos(60°): {exact_cos}")
print(f"Погрешность: {abs(exact_cos - approx_cos)}")

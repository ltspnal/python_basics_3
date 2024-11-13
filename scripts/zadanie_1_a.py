import math


def taylor_sin(x, terms=10):
    result = 0
    for n in range(terms):
        term = ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
        result += term
    return result


x = math.radians(30)
approx_sin = taylor_sin(x, terms=10)
exact_sin = math.sin(x)

print(f"Приближённое значение sin(30°): {approx_sin}")
print(f"Точное значение sin(30°): {exact_sin}")
print(f"Погрешность: {abs(exact_sin - approx_sin)}")

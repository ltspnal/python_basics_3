def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


n = 10
sequence = fibonacci_sequence(n)
print(f"Первые {n} чисел Фибоначчи: {sequence}")

def analyze_list(numbers):
    total_sum = sum(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    return total_sum, min_value, max_value


numbers = [10, 20, -5, 0, 15, 30]
total, minimum, maximum = analyze_list(numbers)

print(f"Список чисел: {numbers}")
print(f"Сумма всех чисел: {total}")
print(f"Минимальное число: {minimum}")
print(f"Максимальное число: {maximum}")

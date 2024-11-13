from collections import Counter


def check_unique_numbers(numbers):
    counts = Counter(numbers)
    duplicates = {num: count for num, count in counts.items() if count > 1}

    if duplicates:
        return False, duplicates
    return True, {}


numbers = [1, 2, 3, 4, 5, 2, 3, 6]
are_unique, duplicates = check_unique_numbers(numbers)

if are_unique:
    print("Все числа в списке уникальны.")
else:
    print("Не все числа уникальны.")
    print("Дублирующиеся элементы и их количество:")
    for num, count in duplicates.items():
        print(f"{num}: встречается {count} раз(а)")

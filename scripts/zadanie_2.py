def calculate_days_to_save(N, k):
    saved = 0
    days = 0
    while saved < N:
        if days % 7 != 6:
            saved += k
        days += 1
    return days


N = 1000
k = 100

days = calculate_days_to_save(N, k)
print(f"Маша накопит {N} рублей за {days} дней.")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

position = binary_search(sorted_list, target)

if position != -1:
    print(f"Элемент {target} найден на позиции {
          position} (индекс {position}).")
else:
    print(f"Элемент {target} не найден в списке.")

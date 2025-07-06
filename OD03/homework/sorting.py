# OD03: Алгоритмы сортировки

# 1. Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


# 2. Сортировка выбором
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 3. Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# 4. Быстрая сортировка (рекурсивная)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = list(filter(lambda x: x < pivot, arr))
    center = [x for x in arr if x == pivot]
    right = list(filter(lambda x: x > pivot, arr))
    return quick_sort(left) + center + quick_sort(right)


# Тестовые данные и вызов функций
original = [5, 7, 4, 3, 8, 2]

# Пузырьковая
bubble = original.copy()
bubble_sort(bubble)
print("Bubble sort:", bubble)

# Выбором
selection = original.copy()
selection_sort(selection)
print("Selection sort:", selection)

# Вставками
insertion = original.copy()
insertion_sort(insertion)
print("Insertion sort:", insertion)

# Быстрая
quick = original.copy()
sorted_quick = quick_sort(quick)
print("Quick sort:", sorted_quick)

# OD04: Анализ сложности — проект по продаже свечей

# Сценарий: сортировка заказов по дате и статусу

def sort_orders(orders):
    """
    Сортировка заказов по дате (по убыванию) и статусу (выполненные — первыми).
    Пример: [{'date': '2025-07-01', 'status': 'done'}]
    """
    return sorted(orders, key=lambda x: (-x['date'].toordinal(), x['status'] != 'done'))

# Пример входных данных
from datetime import date

orders = [
    {'id': 1, 'date': date(2025, 7, 1), 'status': 'pending'},
    {'id': 2, 'date': date(2025, 7, 3), 'status': 'done'},
    {'id': 3, 'date': date(2025, 7, 2), 'status': 'done'},
    {'id': 4, 'date': date(2025, 7, 3), 'status': 'pending'},
]

sorted_orders = sort_orders(orders)
for order in sorted_orders:
    print(order)

"""
Анализ сложности:

Временная сложность:
- sorted() использует Timsort → O(n log n)
- key=lambda ... — доступ по ключу словаря и преобразование → O(1)
=> Итог: O(n log n)

Пространственная сложность:
- sorted() возвращает новый список → O(n)

Вывод: Алгоритм эффективен и масштабируем даже для 10 000+ заказов.
"""

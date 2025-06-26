class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавить элемент в стек"""
        self.items.append(item)

    def pop(self):
        """Удалить и вернуть верхний элемент"""
        return self.items.pop() if self.items else None

    def peek(self):
        """Посмотреть верхний элемент"""
        return self.items[-1] if self.items else None

    def is_empty(self):
        """Проверить, пуст ли стек"""
        return not self.items

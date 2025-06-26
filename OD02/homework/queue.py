class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавить в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удалить и вернуть первый элемент"""
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return not self.items

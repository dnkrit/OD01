class Graph:
    def __init__(self):
        self.graph = {}  # словарь смежности

    def add_edge(self, u, v):
        """Добавить связь между вершинами"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

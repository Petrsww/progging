class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1

    def bpm(self, u, match_r, seen):
        for v in range(self.V):
            if self.graph[u][v] and not seen[v]:
                seen[v] = True
                if match_r[v] == -1 or self.bpm(match_r[v], match_r, seen):
                    match_r[v] = u
                    return True
        return False

    def max_bipartite_matching(self):
        match_r = [-1] * self.V
        result = 0
        for i in range(self.V):
            seen = [False] * self.V
            if self.bpm(i, match_r, seen):
                result += 1
        return result

# Пример использования
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Размер максимального паросочетания:", g.max_bipartite_matching())

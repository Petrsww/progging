class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

def kruskal(edges, n):
    tree = []
    edges.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(n)

    for edge in edges:
        if disjoint_set.union(edge[0], edge[1]):
            tree.append(edge)

    return set([(min(edge[0], edge[1]), max(edge[0], edge[1])) for edge in tree])

def determine_edge_status(n, m, edges):
    mst_edges = kruskal(edges, n)
    
    result = []
    for edge in edges:
        if (min(edge[0], edge[1]), max(edge[0], edge[1])) in mst_edges:
            result.append("any")
        else:
            result.append("at least one")        

    return result

# Чтение входных данных
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((a - 1, b - 1, w))

# Получение ответов для ребер
answers = determine_edge_status(n, m, edges)

# Вывод ответов
for answer in answers:
    print(answer)

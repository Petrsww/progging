from collections import defaultdict
from collections import deque

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in graph if in_degree[u] == 0])
    result = {u: 0 for u in graph}
    result[v] = 1

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            result[v] += result[u]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result[u]

graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]  
for edge in edges:
    graph[edge[0]].append(edge[1])

v, u = 1, 4
result = topological_sort(graph)

print(f"Количество путей из вершины {v} в вершину {u}: {result}")

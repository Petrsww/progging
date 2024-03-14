from collections import defaultdict

def build_tree(graph, parent, node):
    parent[node] = node
    for child in graph[node]:
        build_tree(graph, parent, child)
        parent[child] = node

def is_ancestor(parent, u, v):
    while v != u:
        if v == parent[v]:
            return False
        v = parent[v]
    return True


n = 5  
graph = defaultdict(list)
edges = [(1, 2), (1, 3), (2, 4), (3, 5)]  
for edge in edges:
    graph[edge[0]].append(edge[1])

parent = {}
build_tree(graph, parent, 1)  

queries = [(2, 4), (1, 5)]
for query in queries:
    u, v = query
    result = is_ancestor(parent, u, v)
    print(f"Вершина {u} {'является' if result else 'не является'} предком вершины {v}")

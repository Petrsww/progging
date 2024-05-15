INF = float('inf')

def bellman_ford(graph, start):
    distances = {node: INF for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                if distances[node] + graph[node][neighbor] < distances[neighbor]:
                    distances[neighbor] = distances[node] + graph[node][neighbor]

    for node in graph:
        for neighbor in graph[node]:
            if distances[node] + graph[node][neighbor] < distances[neighbor]:
                return "Negative cycle detected"

    return distances

graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

start_node = 'A'
result = bellman_ford(graph, start_node)

for node in result:
    if result[node] == INF:
        print(f"Distance from {start_node} to {node}: inf")
    else:
        print(f"Distance from {start_node} to {node}: {result[node]}")

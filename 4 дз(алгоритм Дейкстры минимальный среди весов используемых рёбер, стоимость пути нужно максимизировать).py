import heapq

def dijkstra_min_edge_weight_maximize_path(graph, start):
    distances = {node: float('-inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance < distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_distance = min(current_distance, weight)
            if new_distance > distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

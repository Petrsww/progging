import heapq

def dijkstra_edge_weight_product(graph, start):
    distances = {node: 1 for node in graph}
    distances[start] = 1
    queue = [(1, start)]

    while queue:
        current_product, current_node = heapq.heappop(queue)

        if current_product > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_product = current_product * weight
            if new_product < distances[neighbor]:
                distances[neighbor] = new_product
                heapq.heappush(queue, (new_product, neighbor))

    return distances

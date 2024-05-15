def check_constraints(array_len, constraints):
    graph = []
    for i in range(1, 2**array_len):
        array = [1 if i & (1 << j) else -1 for j in range(array_len)]
        graph.append(array)

    for constraint in constraints:
        for i in range(len(graph)):
            for j in range(len(graph)):
                if constraint[2] < 0:
                    weight = sum(graph[j][constraint[0]-1:constraint[1]]) + constraint[2]
                else:
                    weight = sum(graph[j][constraint[0]-1:constraint[1]]) - constraint[2]
                graph[i][j] = min(graph[i][j], weight)

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] < 0:
                return False
    return True

# Пример использования
array_len = 5
constraints = [(1, 3, 2), (2, 4, -3)]

if check_constraints(array_len, constraints):
    print("Существует загаданный массив удовлетворяющий ограничениям.")
else:
    print("Загаданный массив не существует удовлетворяющий ограничениям.")

import heapq

def dijkstra_with_paths(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если найден более короткий путь то пропускаем
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    paths = {}
    for vertex in graph:
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        paths[vertex] = list(reversed(path))

    return distances, paths


#Граф под который рассчитывасем расстояния
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
    'E': [('C', 8), ('D', 3)],
    'F': [('D', 6)]
}

start_vertex = 'A'
distances, paths = dijkstra_with_paths(graph, start_vertex)

print(f"Кратчайшие пути от вершины {start_vertex}:")
for vertex in graph:
    path_str = " → ".join(paths[vertex])
    print(f"До {vertex}: расстояние = {distances[vertex]}, путь = {path_str}")

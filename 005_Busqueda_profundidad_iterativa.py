def iddfs(graph, start, goal):
    for max_depth in range(len(graph)):
        visited = set()
        if dls(graph, start, goal, max_depth, visited):
            return True
    return False

def dls(graph, node, goal, max_depth, visited):
    if max_depth < 0:
        return False

    if node == goal:
        return True

    if max_depth == 0:
        return False

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if dls(graph, neighbor, goal, max_depth - 1, visited):
                return True

    visited.remove(node)
    return False

# Ejemplo de grafo dirigido
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

print(f"Búsqueda en Profundidad Iterativa para encontrar el objetivo '{goal_node}':")
found = iddfs(graph, start_node, goal_node)

if found:
    print(f"¡Se encontró el objetivo '{goal_node}'!")
else:
    print(f"No se encontró el objetivo '{goal_node}' en el grafo.")


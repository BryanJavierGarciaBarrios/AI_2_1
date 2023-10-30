def ldfs_with_goal(graph, node, depth, limit, goal):
    if depth > limit:
        return False
    print(node, end=' ')
    
    if node == goal:
        return True
    
    for neighbor in graph[node]:
        if ldfs_with_goal(graph, neighbor, depth + 1, limit, goal):
            return True
    
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
max_depth = 2  # Profundidad máxima permitida
goal_node = 'F'  # Nodo objetivo

print(f"Recorrido en Profundidad Limitada con objetivo '{goal_node}' (hasta profundidad {max_depth}):")
found = ldfs_with_goal(graph, start_node, 0, max_depth, goal_node)

if found:
    print(f"\n¡Se encontró el objetivo '{goal_node}'!")
else:
    print(f"\nNo se encontró el objetivo '{goal_node}' dentro del límite de profundidad.")

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

def bidirectional_search(graph, start, goal):
    forward_visited = {start: None}
    backward_visited = {goal: None}
    forward_queue = [start]
    backward_queue = [goal]

    while forward_queue and backward_queue:
        intersection_node = intersection(forward_visited, backward_visited)
        if intersection_node is not None:
            return path_to_goal(forward_visited, backward_visited, intersection_node)

        expand_node(forward_queue, forward_visited, graph)
        expand_node(backward_queue, backward_visited, graph)

    return None

def intersection(visited1, visited2):
    for node in visited1:
        if node in visited2:
            return node
    return None

def expand_node(queue, visited, graph):
    current = queue.pop(0)
    for neighbor in graph.graph[current]:
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)

def path_to_goal(forward_visited, backward_visited, intersection_node):
    path = []
    while intersection_node is not None:
        path.append(intersection_node)
        intersection_node = forward_visited[intersection_node]

    path = list(reversed(path))
    intersection_node = backward_visited[path[-1]]

    while intersection_node is not None:
        path.append(intersection_node)
        intersection_node = backward_visited[intersection_node]

    return path

# Crear un grafo dirigido para el ejemplo
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('C', 'E')
graph.add_edge('E', 'F')
graph.add_edge('F', 'G')
graph.add_edge('G', 'H')
graph.add_edge('H', 'I')
graph.add_edge('I', 'J')
graph.add_edge('J', 'K')

start_node = 'A'
goal_node = 'K'

print(f"Búsqueda Bidireccional desde '{start_node}' hasta '{goal_node}':")
path = bidirectional_search(graph, start_node, goal_node)

if path:
    print(f"Camino encontrado: {' -> '.join(path)}")
else:
    print("No se encontró un camino entre los nodos.")

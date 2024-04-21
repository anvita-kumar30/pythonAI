def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]
    while queue:
        vertex, path = queue.pop(0)   # Dequeue operation
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            if vertex == goal:
                print("\nPath to goal node:", ' -> '.join(path))
                return
            queue.extend((neighbor, path + [neighbor]) for neighbor in graph[vertex] if neighbor not in visited)

def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        vertex = input(f"Enter vertex {i+1}: ")
        neighbors = input(f"Enter neighbors of {vertex} (comma-separated): ").split(',')
        graph[vertex] = [neighbor.strip() for neighbor in neighbors]
    return graph

if __name__ == "__main__":
    user_graph = create_graph()
    start_vertex = input("Enter the starting vertex for BFS: ")
    goal_vertex = input("Enter the goal vertex: ")
    if start_vertex not in user_graph or goal_vertex not in user_graph:
        print("Invalid starting or goal vertex.")
    else:
        print("\nBFS Traversal: ")
        bfs(user_graph, start_vertex, goal_vertex)
def dls(graph, start, goal, depth, visited):
    if depth >= 0:
        if start not in visited:
            print(start, end=' ')
            visited.add(start)
            if start == goal:
                return True
            for neighbor in graph[start]:
                if dls(graph, neighbor, goal, depth - 1, visited):
                    return True
    return False


def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        vertex = input(f"Enter vertex {i + 1}: ")
        neighbors = input(f"Enter neighbors of {vertex} (comma-separated): ").split(',')
        graph[vertex] = [neighbor.strip() for neighbor in neighbors]
    return graph


if __name__ == "__main__":
    user_graph = create_graph()
    start_vertex = input("Enter the starting vertex for DLS: ")
    goal_vertex = input("Enter the goal vertex: ")
    depth_limit = int(input("Enter the depth limit: "))

    if start_vertex not in user_graph or goal_vertex not in user_graph:
        print("Invalid starting or goal vertex.")
    else:
        visited_set = set()
        print("DLS traversal:")
        if not dls(user_graph, start_vertex, goal_vertex, depth_limit, visited_set):
            print("\nGoal node not reachable within the depth limit from the starting node.")

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


def dfid(graph, start, goal):
    depth_limit = 0
    while True:
        print(f"\nSearching with depth limit: {depth_limit}")
        visited_set = set()
        if dls(graph, start, goal, depth_limit, visited_set):
            return True
        depth_limit += 1


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
    start_vertex = input("Enter the starting vertex for DFID: ")
    goal_vertex = input("Enter the goal vertex: ")

    if start_vertex not in user_graph or goal_vertex not in user_graph:
        print("Invalid starting or goal vertex.")
    else:
        print("DFID traversal:")
        if not dfid(user_graph, start_vertex, goal_vertex):
            print("Goal node not reachable from the starting node.")

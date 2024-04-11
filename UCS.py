import heapq


def ucs(graph, start, goal):
    visited = set()
    heap = [(0, start, [start])]  # (cost, vertex, path)
    while heap:
        cost, vertex, path = heapq.heappop(heap)
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            if vertex == goal:
                print("\nPath to goal node:", ' -> '.join(path))
                return
            for neighbor, neighbor_cost in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor, path + [neighbor]))


def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        vertex = input(f"Enter vertex {i + 1}: ")
        neighbors = input(f"Enter neighbors of {vertex} with their costs (comma-separated, neighbor:cost): ").split(',')
        graph[vertex] = {}
        for neighbor_cost_pair in neighbors:
            neighbor, cost = neighbor_cost_pair.split(':')
            graph[vertex][neighbor.strip()] = int(cost.strip())
    return graph


if __name__ == "__main__":
    user_graph = create_graph()
    start_vertex = input("Enter the starting vertex for UCS: ")
    goal_vertex = input("Enter the goal vertex: ")

    if start_vertex not in user_graph or goal_vertex not in user_graph:
        print("Invalid starting or goal vertex.")
    else:
        print("UCS traversal:")
        ucs(user_graph, start_vertex, goal_vertex)

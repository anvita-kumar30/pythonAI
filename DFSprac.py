def dfs(graph, start, goal, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        if start == goal:
            return True
        for neighbor in graph[start]:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

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
    start_vertex = input("Enter the starting vertex for DFS: ")
    goal_vertex = input("Enter the goal vertex: ")
    if start_vertex not in user_graph or goal_vertex not in user_graph:
        print("Invalid starting or goal vertex.")
    else:
        visited_set = set()
        print("DFS traversal: ")
        if not dfs(user_graph, start_vertex, goal_vertex, visited_set):
            print("Goal node not reachable from the starting node.")
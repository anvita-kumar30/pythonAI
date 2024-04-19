class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

def build_tree():
    root_name = input("Enter the name for the root node: ")
    root_value = input("Enter the value for the root node: ")
    root = Node(root_name, root_value)
    queue = [root]

    while queue:
        print("Queue:", [(node.name, node.value) for node in queue])
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.name} ({current_node.value}): "))

        for i in range(num_children):
            child_name = input(f"Enter the name for child {i + 1} of node {current_node.name}: ")
            child_value = input(f"Enter the value for child {i + 1} of node {current_node.name}: ")
            child_node = Node(child_name, child_value)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

def heuristic(node, goal):
    return abs(ord(node.name) - ord(goal))

def greedy_bfs(root, start, goal):
    queue = [root]
    path = []

    while queue:
        print("Queue:", [(node.name, node.value) for node in queue])
        current_node = queue.pop(0)
        path.append((current_node.name, current_node.value))

        if current_node.name == goal:
            print("Goal reached!")
            break

        if current_node.children:
            queue = sorted(queue + current_node.children, key=lambda x: x.value)
        print("Path:", path)
    return path

def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Greedy BFS traversal:", greedy_bfs(root, start_node, goal_node))

if __name__ == "__main__":
    main()

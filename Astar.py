class Node:
    def __init__(self, name, value, heuristic):
        self.name = name
        self.value = value
        self.heuristic = heuristic
        self.children = []

    def __lt__(self, other):
        return (self.value + self.heuristic) < (other.value + other.heuristic)


def build_tree():
    root_name = input("Enter the name for the root node: ")
    root_value = int(input("Enter the value for the root node: "))
    root_heuristic = int(input("Enter the heuristic value for the root node: "))
    root = Node(root_name, root_value, root_heuristic)
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.name} ({current_node.value}): "))
        for i in range(num_children):
            child_name = input(f"Enter the name for child {i + 1} of node {current_node.name}: ")
            child_value = int(input(f"Enter the value for child {i + 1} of node {current_node.name}: "))
            child_heuristic = int(input(f"Enter the heuristic value for child {i + 1} of node {current_node.name}: "))
            child_node = Node(child_name, child_value, child_heuristic)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root


def astar(root, start, goal):
    open_set = [root]
    closed_set = set()
    path = []
    i = 0
    while open_set:
        print("Open Set (Nodes to Explore) after iteration {i+1}:")
        print([(node.name, node.value, node.heuristic) for node in open_set])
        print("Closed Set (Nodes Fully Explored) after iteration {i+1}:")
        print([(node.name, node.value, node.heuristic) for node in closed_set])
        print("------------------------------")
        current_node = open_set.pop(0)
        path.append((current_node.name, current_node.value))
        i = i + 1
        if current_node.name == goal:
            print("Goal reached!")
            break

        closed_set.add(current_node)

        for child in current_node.children:
            if child not in closed_set and child not in open_set:
                open_set.append(child)
                # Optionally, you can sort open_set based on heuristic value:
                open_set.sort(key=lambda x: x.heuristic)
    return path


def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    print("Starting A* traversal from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")

    final_path = astar(root, start_node, goal_node)

    print("------------------------------")
    print("Final Path (Nodes Visited):", final_path)


if __name__ == "__main__":
    main()

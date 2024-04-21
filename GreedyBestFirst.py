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
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.name} ({current_node.value}): "))
        for i in range(num_children):
            child_name = input(f"Enter the name for child {i + 1} of node {current_node.name}: ")
            child_value = input(f"Enter the value for child {i + 1} of node {current_node.name}: ")
            child_node = Node(child_name, child_value)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

def greedy_bfs(root, start, goal):
    open_list = [root]
    closed_list = []
    i=0
    while open_list:
        print(f"Open List (Nodes to Explore) after iteration {i+1}:")
        print([(node.name, node.value) for node in open_list])
        print(f"Closed List (Nodes Fully Explored) after iteration {i+1}:")
        print([(node.name, node.value) for node in closed_list])
        print("------------------------------")
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        i = i + 1
        if current_node.name == goal:
            print("Goal reached!")
            break
        if current_node.children:
            # Sort the children based on heuristic value for Greedy BFS
            sorted_children = sorted(current_node.children, key=lambda x: x.value)
            open_list = sorted_children + open_list
    # Return only the final path
    final_path = [(node.name, node.value) for node in closed_list]
    return final_path


def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Starting Greedy BFS traversal from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")
    final_path = greedy_bfs(root, start_node, goal_node)
    print("------------------------------")
    print("Final Path (Nodes Visited):", final_path)

if __name__ == "__main__":
    main()

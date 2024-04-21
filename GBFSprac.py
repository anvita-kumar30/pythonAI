class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []

def build_tree():
    root_name = input("Enter the name for the root node: ")
    root_heuristic = float(input("Enter the heuristic value for the root node: "))
    root = Node(root_name, root_heuristic)
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
        for i in range(num_children):
            child_name = input(f"Enter the name of child {i+1} of node {current_node.name}: ")
            child_heuristic = float(input(f"Enter the heuristic value for child {i+1} of node {current_node.name}: "))
            child_node = Node(child_name, child_heuristic)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

def gbfs(root, start, goal):
    open_list = [root]
    closed_list = []
    i = 0
    while open_list:
        print(f"Open list (Nodes to explore) after iteration {i+1}: ")
        print([node.name for node in open_list])
        print(f"Closed List (Nodes fully explored) after iteration {i+1}: ")
        print([node.name for node in closed_list])
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        i += 1
        if current_node.name == goal:
            print("Goal reached!")
            break
        if current_node.children:
            sorted_children = sorted(current_node.children, key=lambda x: x.heuristic)
            open_list = sorted_children + open_list
    final_path = [node.name for node in closed_list]
    return final_path

def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Starting Greedy Best-First Search (GBFS) from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")
    final_path = gbfs(root, start_node, goal_node)
    print("------------------------------")
    print("Final Path:", final_path)

if __name__ == "__main__":
    main()

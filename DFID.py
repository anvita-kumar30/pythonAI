class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
def build_tree():
    root_name = input("Enter the name for the root node: ")
    root = Node(root_name)
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
        for i in range(num_children):
            child_name = input(f"Enter the name of child {i + 1} of node {current_node.name}: ")
            child_node = Node(child_name)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root
def dls(root, goal, depth_limit, current_depth=0):
    open_list = [(root, current_depth)]
    closed_list = []
    i = 0
    while open_list:
        print(f"Open list (Nodes to explore) after iteration {i + 1}:")
        print([(node.name, depth) for node, depth in open_list])
        print(f"Closed List (Nodes fully explored) after iteration {i + 1}:")
        print([node.name for node in closed_list])
        print("------------------------------")
        current_node, node_depth = open_list.pop(0)
        closed_list.append(current_node)
        i += 1
        if current_node.name == goal:
            print("Goal reached!")
            break
        if node_depth < depth_limit and current_node.children:
            sorted_children = sorted(current_node.children, key=lambda x: x.name)
            open_list = [(child, node_depth + 1) for child in sorted_children] + open_list
    final_path = [node.name for node in closed_list]
    return final_path
def dfid(root, start, goal):
    max_depth = 0
    while True:
        print(f"Exploring with depth limit: {max_depth}")
        final_path = dls(root, goal, max_depth)

        if goal in final_path:
            return final_path
        max_depth += 1
def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Starting Depth-First Iterative Deepening (DFID) from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")
    final_path = dfid(root, start_node, goal_node)
    if final_path:
        print("------------------------------")
        print("Path Found:", final_path)
    else:
        print("Goal node not reachable within the depth limit.")
if __name__ == "__main__":
    main()

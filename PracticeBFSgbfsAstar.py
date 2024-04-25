#BFS
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

def bfs(root, start, goal):
    open_list = [root]
    closed_list = []
    i = 0
    while open_list:
        print(f"Open list (Nodes to explore) after iteration {i + 1}:")
        print([(node.name) for node in open_list])
        print(f"Closed List (Nodes fully explored) after iteration {i + 1}:")
        print([(node.name) for node in closed_list])
        print("------------------------------")
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        i += 1
        if current_node.name == goal:
            print("Goal reached!")
            break
        for child in current_node.children:
            if child not in open_list and child not in closed_list:
                open_list.append(child)
    final_path = [(node.name) for node in closed_list]
    return final_path

def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Starting BFS traversal from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")
    final_path = bfs(root, start_node, goal_node)
    print("------------------------------")
    print("Final Path (Nodes Visited):", final_path)

if __name__ == "__main__":
    main()

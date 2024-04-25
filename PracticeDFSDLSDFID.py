#DFS
# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
# def build_tree():
#     root_name = input("Enter the root node of the tree: ")
#     root = Node(root_name)
#     queue = [root]
#     while queue:
#         current_node = queue.pop(0)
#         num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
#         for i in range(num_children):
#             child_name = input(f"Enter the name of child {i+1} of node {current_node.name}: ")
#             child_node = Node(child_name)
#             current_node.children.append(child_node)
#             queue.append(child_node)
#     return root
# def dfs(root, start, goal):
#     open_list = [root]
#     closed_list = []
#     i=0
#     while open_list:
#         print(f"Open List (Nodes to explore) after iteration {i+1}: ")
#         print([(node.name) for node in open_list])A
#
#         print(f"Closed List (Nodes fully explored) after iteration {i+1}: ")
#         print([(node.name) for node in closed_list])
#         print("-----------------")
#         current_node = open_list.pop(0)
#         closed_list.append(current_node)
#         i+=1
#         if current_node.name==goal:
#             print("\nGoal Reached!")
#             break
#         if current_node.children:
#             sorted_children = sorted(current_node.children, key=lambda x: x.name)
#             open_list = sorted_children + open_list
#     final_path = [(node.name) for node in closed_list]
#     return final_path
# def main():
#     root = build_tree()
#     start_node = input("Enter the start node: ")
#     goal_node = input("Enter the goal node: ")
#     print("-----------------")
#     print("\nDFS Traversal: ")
#     final_path = dfs(root, start_node, goal_node)
#     print("\nFinal Path: ", final_path)
#
# if __name__ == "__main__":
#     main()

#DLS
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
def build_tree():
    root_name = input("Enter the root node of the tree: ")
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


def dfs(root, start, goal, depth_limit, current_depth=0):
    open_list = [(root, current_depth)]
    closed_list = []
    i = 0
    while open_list:
        print(f"Open List (Nodes to explore) after iteration {i + 1}: ")
        print([(node.name, depth) for node, depth in open_list])
        print(f"Closed List (Nodes fully explored) after iteration {i + 1}: ")
        print([(node.name) for node in closed_list])
        print("-----------------")
        current_node, node_depth = open_list.pop(0)
        closed_list.append(current_node)
        i += 1
        if current_node.name == goal:
            print("\nGoal Reached!")
            break
        if node_depth < depth_limit and current_node.children:
            sorted_children = sorted(current_node.children, key=lambda x: x.name)
            open_list = [(child, node_depth+1) for child in sorted_children] + open_list
    final_path = [(node.name) for node in closed_list]
    return final_path


def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    depth_limit = int(input("Enter the depth limit: "))
    print("-----------------")
    print("\nDLS Traversal: ")
    final_path = dfs(root, start_node, goal_node, depth_limit)
    print("\nFinal Path: ", final_path)


if __name__ == "__main__":
    main()
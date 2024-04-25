#BFS
# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []
#
# def build_tree():
#     root_name = input("Enter the name for the root node: ")
#     root = Node(root_name)
#     queue = [root]
#     while queue:
#         current_node = queue.pop(0)
#         num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
#         for i in range(num_children):
#             child_name = input(f"Enter the name of child {i + 1} of node {current_node.name}: ")
#             child_node = Node(child_name)
#             current_node.children.append(child_node)
#             queue.append(child_node)
#     return root
#
# def bfs(root, start, goal):
#     open_list = [root]
#     closed_list = []
#     i = 0
#     while open_list:
#         print(f"Open list (Nodes to explore) after iteration {i + 1}:")
#         print([(node.name) for node in open_list])
#         print(f"Closed List (Nodes fully explored) after iteration {i + 1}:")
#         print([(node.name) for node in closed_list])
#         print("------------------------------")
#         current_node = open_list.pop(0)
#         closed_list.append(current_node)
#         i += 1
#         if current_node.name == goal:
#             print("Goal reached!")
#             break
#         for child in current_node.children:
#             if child not in open_list and child not in closed_list:
#                 open_list.append(child)
#     final_path = [(node.name) for node in closed_list]
#     return final_path
#
# def main():
#     root = build_tree()
#     start_node = input("Enter the start node: ")
#     goal_node = input("Enter the goal node: ")
#     print("Starting BFS traversal from node", start_node)
#     print("Goal node is", goal_node)
#     print("------------------------------")
#     final_path = bfs(root, start_node, goal_node)
#     print("------------------------------")
#     print("Final Path (Nodes Visited):", final_path)
#
# if __name__ == "__main__":
#     main()

#GBFS
# class Node:
#     def __init__(self, name, heuristic):
#         self.name = name
#         self.heuristic = heuristic
#         self.children = []
#
# def build_tree():
#     root_name = input("Enter the name for the root node: ")
#     root_heuristic = float(input("Enter the heuristic value for the root node: "))
#     root = Node(root_name, root_heuristic)
#     queue = [root]
#     while queue:
#         current_node = queue.pop(0)
#         num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
#         for i in range(num_children):
#             child_name = input(f"Enter the name of child {i + 1} of node {current_node.name}: ")
#             child_heuristic = float(input(f"Enter the heuristic value for child {i+1} of node {current_node.name}: "))
#             child_node = Node(child_name, child_heuristic)
#             current_node.children.append(child_node)
#             queue.append(child_node)
#     return root
#
# def gbfs(root, start, goal):
#     open_list = [root]
#     closed_list = []
#     i = 0
#     while open_list:
#         print(f"Open list (Nodes to explore) after iteration {i + 1}:")
#         print([(node.name) for node in open_list])
#         print(f"Closed List (Nodes fully explored) after iteration {i + 1}:")
#         print([(node.name) for node in closed_list])
#         print("------------------------------")
#         current_node = open_list.pop(0)
#         closed_list.append(current_node)
#         i += 1
#         if current_node.name == goal:
#             print("Goal reached!")
#             break
#         if current_node.children:
#             sorted_children = sorted(current_node.children, key=lambda x: x.heuristic)
#             open_list = sorted_children + open_list
#     final_path = [(node.name) for node in closed_list]
#     return final_path
#
# def main():
#     root = build_tree()
#     start_node = input("Enter the start node: ")
#     goal_node = input("Enter the goal node: ")
#     print("Starting GBFS traversal from node", start_node)
#     print("Goal node is", goal_node)
#     print("------------------------------")
#     final_path = gbfs(root, start_node, goal_node)
#     print("------------------------------")
#     print("Final Path (Nodes Visited):", final_path)
#
# if __name__ == "__main__":
#     main()

#A star
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
        num_children = int(input(f"Enter the number of children for node {current_node.name}: "))
        for i in range(num_children):
            child_name = input(f"Enter the name of child {i + 1} of node {current_node.name}: ")
            child_value = int(input(f"Enter the value for child {i+1} of node {current_node.name}: "))
            child_heuristic = float(input(f"Enter the heuristic value for child {i+1} of node {current_node.name}: "))
            child_node = Node(child_name, child_value, child_heuristic)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root

def astar(root, start, goal):
    open_list = [root]
    closed_list = []
    i = 0
    while open_list:
        print(f"Open list (Nodes to explore) after iteration {i + 1}:")
        print([(node.name, node.value, node.heuristic) for node in open_list])
        print(f"Closed List (Nodes fully explored) after iteration {i + 1}:")
        print([(node.name) for node in closed_list])
        print("------------------------------")
        current_node = open_list.pop(0)
        closed_list.append(current_node)
        i += 1
        if current_node.name == goal:
            print("Goal reached!")
            break
        if current_node.children:
            sorted_children = sorted(current_node.children, key=lambda x: x.heuristic + x.value)
            open_list = sorted_children + open_list
    final_path = [(node.name) for node in closed_list]
    return final_path

def main():
    root = build_tree()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    print("Starting A star traversal from node", start_node)
    print("Goal node is", goal_node)
    print("------------------------------")
    final_path = astar(root, start_node, goal_node)
    print("------------------------------")
    print("Final Path (Nodes Visited):", final_path)

if __name__ == "__main__":
    main()

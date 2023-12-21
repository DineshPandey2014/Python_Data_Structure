
from collections import deque

# Test class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""
Part 1: Find all parent node. Prepare a dictionary
Part 2: Traverse a tree starting from root
        a) Go left
        b) Go Right
        c) Go Parent
        d) Increment path by 1
        e) Check the path count. If equal to K return. The result
"""
def bfs_find_all_parent_node(root):
    # Here we are creating dictionary which hold parent of the node
    dict = {}
    # Add root node whose parent node is None
    dict[root] = None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left_node = node.left
        right_node = node.right
        # to left and right node to queue
        if left_node:
            queue.append(left_node)
            dict[left_node] = node

        if right_node:
            queue.append(right_node)
            dict[right_node] = node
    return dict


# Here we traverse binary tree as left_node, right_node and it's parent.
# Here path for at each node will get increment by. All are at same level
# will check the path_count. If path_count equals to K
# Need to return all the node which are at distance k from target node
# def find_distance(target_node, dict, k):
#     queue = deque([target_node])
#     visited = set()
#     path = 0
#     result = []
#     while queue:
#         # Here in the Qeue we have a all the nodes that are K distance apart
#         # From queue which is deque we will get the list of node
#         if path == k:
#             return list(queue)
#         node = queue.popleft()
#         # Visited when it got pop from queue
#         if node not in visited:
#             visited.add(node)
#             path = path + 1
#             # Traverse Left
#             if node.left and node.left not in visited:
#                 queue.append(node.left)
#             # Traverse Right
#             if node.right and node.right not in visited:
#                 queue.append(node.right)
#             #Traverse parent
#             parent = dict[node]
#             if parent:
#                 queue.append(parent)

def find_distance(target_node, dict, k):
    queue = deque([(target_node, 0)])
    visited = set()
    # path = 0
    result = []
    while queue:
        node, distance = queue.popleft()
        # Here in the Qeue we have a all the nodes that are K distance apart
        # From queue which is deque we will get the list of node
        if distance == k:
            return list(queue)

        # Visited when it got pop from queue
        if node not in visited:
            visited.add(node)
            # path = path + 1
            # Traverse Left
            if node.left and node.left not in visited:
                queue.append((node.left, distance + 1))
            # Traverse Right
            if node.right and node.right not in visited:
                queue.append((node.right, distance + 1))
            # Traverse parent
            parent = dict[node]
            if parent:
                queue.append((parent, distance + 1))

# parent_dict = bfs_find_all_parent_node(root)
# list_node_at_k_distance = find_distance(target, parent_dict, k)
# result = [node.val for node in list_node_at_k_distance]
# return result

if __name__ == "__main__":
    # Create a sample binary tree for testing
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    target_node = root.left.right # Find node ->4
    parent_dict = bfs_find_all_parent_node(root)
    k = 2
    list_node_at_k_distance = find_distance(target_node, parent_dict, k)
    result = [node for node in list_node_at_k_distance]
    print(result)

    # print(parent_dict)
    # k = 2
    # distance = find_distance(root, parent_dict, k)
    # print(distance)


    def test_node_found(self):
        target_node = self.root.left.right
        result = bfs_find_all_parent_node(root)
        self.assertEqual(result, target_node)

    def test_node_not_found(self):
        target_node = TreeNode(6)  # Assuming this node is not in the tree
        result = bfs_find_all_parent_node(root )
        self.assertIsNone(result)


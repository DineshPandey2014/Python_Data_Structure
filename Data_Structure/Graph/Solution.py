from collections import deque


class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bfs_find_all_parent_node(root, target):
    if root == target:
        return [root.val]
    # Here we are creating dictionary which hold parent of the node
    parent_dict = {}
    # Add root node whose parent node is None
    parent_dict[root] = None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        left_node = node.left
        right_node = node.right
        # to left and right node to queue
        if left_node:
            queue.append(left_node)
            parent_dict[left_node] = node

        if right_node:
            queue.append(right_node)
            parent_dict[right_node] = node
    return parent_dict

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
            # Here we need to add the node and distance back to queue because that node is at distance k
            # important it's tuple that we are adding to qeue
            queue.append((node, distance))
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
            if parent and parent not in visited:
                queue.append((parent, distance + 1))

"""
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
"""
if __name__ == "__main__":
    # root = Tree(3)
    # root.left = Tree(5)
    # root.left.left = Tree(6)
    # root.left.right= Tree(2)
    # root.left.right.left = Tree(7)
    # root.left.right.right = Tree(4)
    # root.right = Tree(1)
    # root.right.left = Tree(0)
    # root.right.left = Tree(8)
    #
    #
    # k = 2
    # parent_dict = bfs_find_all_parent_node(root, root.left)
    # list_node_at_k_distance = find_distance(root.left , parent_dict, k)
    # # List of tuple
    # result = []
    # for node, distance in list_node_at_k_distance:
    #     result.append(node.val)
    # print(result)

    root = Tree(0)
    root.right = Tree(1)
    root.right.right = Tree(2)
    root.right.right.right = Tree(3)
    root.right.right.right.right = Tree(4)

    k = 2
    target = root
    parent_dict = bfs_find_all_parent_node(root, root.right.right )
    list_node_at_k_distance = find_distance(target , parent_dict, k)
    # List of tuple
    result = []
    for node, distance in list_node_at_k_distance:
        result.append(node.val)
    print(result)


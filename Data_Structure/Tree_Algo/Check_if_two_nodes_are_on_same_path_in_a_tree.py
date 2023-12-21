"""
https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree-set-2/

Given two nodes of a binary tree v1 and v2, the task is to check if two nodes are on the same path in a tree.
Example:


Input:  v1 = 1, v2 = 5
       1
    /  |  \
   2   3   4
  /    |    \
 5     6     7

Output: Yes
Explanation:
Both nodes 1 and 5
lie in the path 1 -> 2 -> 5.

Input: v1 = 2, v2 = 6
       1
    /  |  \
   2   3   4
  /    |    \
 5     6     7

Output: NO

LCA Approach: The idea is to use Lowest Common Ancestor. Find the LCA of the given vertices v1 and v2.
If the LCA is equal to any of the given two vertices, print Yes. Otherwise, print No.
Below is the implementation of above approach:

"""

"""
Algo: Find LCA. Check the returning node. IF the returnig node is one of them
"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def find_LCA (root, p, q):
    if root == None or root == p or root == q:
        return root

    left_node = find_LCA (root.left, p, q)
    right_node = find_LCA (root.right, p, q)

    if left_node == None:
        return right_node
    elif right_node == None:
        return left_node
    else:
        return root

def check_if_two_nodes_in_same_path(root, p, q):
    lca = find_LCA(root, p, q)

    if lca == p or lca == q:
        return True
    else:
        return False

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #    /     \
    #   4      3
    #        /
    #       7
    #
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(7)
    # Find the LCA for node 3 and 7
    # It should be 3
    result = check_if_two_nodes_in_same_path(root, root.left, root.right.left)
    print(result)

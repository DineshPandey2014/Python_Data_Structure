"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Minimum Depth of Binary Tree
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def minDepth(self, root):
        if root is None:
            return 0

        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)

        # If either left or right subtree is empty,
        # return the non-empty subtree's depth
        if left_height == 0 or right_height == 0:
            return 1 + max(left_height, right_height)

        return 1 + min(left_height, right_height)

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #        /
    #       4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    tree = TreeNode(root)
    result = tree.minDepth(root)
    print(result)
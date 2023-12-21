"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.
"""


def maxDepth(root) -> int:
    def find_max_depth(root):
        if root == None:
            return 0

        left_height = find_max_depth(root.left)

        right_height = find_max_depth(root.right)

        height = max(left_height, right_height)

        return height + 1

    return find_max_depth(root)
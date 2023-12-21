"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

https://www.youtube.com/watch?v=6aChG_3jMAQ

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down
to the nearest leaf node.

Note: A leaf is a node with no children.
"""


class Solution:
    def minDepth(self, root) -> int:

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return 1 + self.minDepth(root.right)
        elif root.right == None and root.left != None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left), )
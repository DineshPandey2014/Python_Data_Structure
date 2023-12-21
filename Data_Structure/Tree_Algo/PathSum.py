"""
https://leetcode.com/problems/path-sum/submissions/

Given the root of a binary tree and an integer targetSum, return true
if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""


def hasPathSum(root, targetSum):
    if root == None:
        return False

    targetSum = targetSum - root.val

    if root.left == None and root.right == None and targetSum == 0:
        return True

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)
"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
Given the root of a binary tree, return the preorder traversal of its nodes' values.

"""
def preorderTraversal(root):
    """
    1) Add the node to the stack.
    Inside while loop till stack is empty
    2) Pop the node.
       In Preorder read the value.
    3) Add the right Tree to stack
    4) Add the left Tree to stack
    """
    if root == None:
        return []

    stack = []
    stack.append(root)
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result






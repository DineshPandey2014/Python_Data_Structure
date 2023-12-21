"""
https://leetcode.com/problems/boundary-of-binary-tree/description/
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.
"""


def boundaryOfBinaryTree(root):
    def left_boundary(root, result):
        if root == None:
            return

        if root.left:
            result.append(root.val)
            left_boundary(root.left, result)
        elif root.right:
            result.append(root.val)
            left_boundary(root.right, result)

    def right_boundary(root, result):
        if root == None:
            return

        if root.right:
            right_boundary(root.right, result)
            result.append(root.val)
        elif root.left:
            right_boundary(root.left, result)
            result.append(root.val)

    def leave_node(root, result):
        if root == None:
            return
        if root.left == None and root.right == None:
            result.append(root.val)
        leave_node(root.left, result)
        leave_node(root.right, result)

    if not root:
        return []


    result = []
    result.append(root.val)
    if root.left:
        left_boundary(root.left, result)
    if root.left or root.right:
        leave_node(root, result)
    if root.right:
        right_boundary(root.right, result)
    return result
"""
https://www.youtube.com/watch?v=0ca1nvR0be4


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


Boundary Traversal :-

 1) Clock wise
2) Anti Clock Wise

Explaination :- For Anti Clockwise

Split the traversal into three parts

1) Add root node to the result
2) Left view except leave node (Print Left Nodes)
3) Leave nodes                 (Print Leave Nodes)
4) Right view except leave nodes (Print Right Nodes)

a) First add the root node to the result
b) Add node values for left keep going if there is left node
   Else go to right node. Inside while loop or recursion
c) If it is leave nodes

#        2
#      /  \
#     1     3
     /    /   \
    0    90     5
             /
            88
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# For anti clock wise traversal first we add the value to result and then we go to left.
# If left is None then we go to right
# For anti clock wise for left side traversal we need to go from top to bottom
def left_boundary(root, result):
    if root == None:
        return

    if root.left:
        result.append(root.val)
        left_boundary(root.left, result)
    elif root.right:
        result.append(root.val)
        left_boundary(root.right, result)

# For anti clock wise traversal first we go to right. And then add the root.val to result
# Then check left go left and then add elements.
# Here for anti clockwise we move from bottom to top
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

"""

#        2
#      /  \
#     1     3
     /    /   \
    0    90     5
             /
            88
"""
if __name__ == "__main__":
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    node.right.left = TreeNode(90)
    node.left.left = TreeNode(0)
    node.right.right = TreeNode(5)
    node.right.right.left = TreeNode(88)
    result = []
    # Here we add the root value first
    result.append(node.val)
    if node.left:
        left_boundary(node.left, result)
    if node.left or node.right:
        leave_node(node, result)
    if node.right:
        right_boundary(node.right, result)
    print(result)

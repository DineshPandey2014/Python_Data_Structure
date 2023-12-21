"""
https://www.youtube.com/watch?v=_-QHfMDde90&t=334s

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a
node to be a descendant of itself).”



"""


# # If left retunrs None and right returns None return root means returning None
# # If root == p => Found the node which has same element as p return root means returnining the node which has
# same element p
# If root == p => Found the node which has same element sa q return root means returning the node which has
# same element q

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None



def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    if root == None or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)

    right = lowestCommonAncestor(root.right, p, q)

    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #        \
    #         3
    #        /
    #       7
    #
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(7)
    # Find the LCA for node 3 and 7
    # It should be 3
    lowestCommonAncestor(root, root.right, root.right.left)
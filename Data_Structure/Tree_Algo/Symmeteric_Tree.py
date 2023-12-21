"""
Is symmeteric is same as two tree for mirror

https://leetcode.com/problems/symmetric-tree/description/

https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

def isSymmetric(root) -> bool:
    """
        1) To check if two tree is mirror of it self. Or one tree is mirrot of other.
        2) To check whether tree is symmeteric around center.
        3) Both are same

        Case1: When two Tree root1 and Tree root2 are given. apply same algorithm
        Case2: When one tree is given apply same algorithm to check is tree isSymmetric.
               Here we have two tree node Tree tree1 (root.left) Tree tree2 (root.right)
    """
    if root == None:
        return True

    def is_symmeteric(root1, root2):
        # if both root are none
        if root1 == root2:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        # For symmeteric check left with right tree
        # Check right with left
        return is_symmeteric(root1.left, root2.right) and is_symmeteric(root1.right, root2.left)

    return is_symmeteric(root.left, root.right)
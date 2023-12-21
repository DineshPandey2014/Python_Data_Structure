"""
226. Invert Binary Tree


https://www.youtube.com/watch?v=dq7pRKEFnFA&list=PLNxqWc8Uj2LRbsOlBiPJZAyZpaUwdDepd&index=26

https://leetcode.com/problems/invert-binary-tree/description/

"""


def invertTree(root):
    """
    ALgo : Here we are returning
    1) check for root as None.
       Return root
    2) Take a temp variable. Assing left node to it.
        Now assign root right node to root left node.
        Inverting means assigning right to left and left to right
        temp = root.left
        root.left = root.right
        root.right = root.left
        call invertTree(for left node)
        call invertTree(for right node)
    """

    if root == None:
        return root

    temp = root.left
    root.left = root.right
    root.right = temp

    # Call recursive for left Tree
    # Call recursive for right Tree
    invertTree(root.left)
    invertTree(root.right)
    return root

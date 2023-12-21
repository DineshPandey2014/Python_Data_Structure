"""
https://practice.geeksforgeeks.org/problems/sum-tree/1

Given a Binary Tree. Return true if, for every node X in the tree other than the leaves,
its value is equal to the sum of its left subtree's value and its right subtree's value. Else return false.

An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0.
A leaf node is also considered a Sum Tree.

"""


def isSumTree(self, root):
    # Code here

    def check_is_sum_tree(root, isSum):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        left_sum = check_is_sum_tree(root.left, isSum)
        right_sum = check_is_sum_tree(root.right, isSum)

        if left_sum + right_sum != root.data:
            isSum[0] = 0
            # To make it faster return 0 form here

        return 2 * root.data if isSum[0] else 0

    # Default it's a sum tree.
    # If any node is not a sum tree, it will keep updating this variable as False
    isSum = [1]
    check_is_sum_tree(root, isSum)
    return isSum[0]
"""
https://www.youtube.com/watch?v=BE2MufZzUWw&list=PLNxqWc8Uj2LRbsOlBiPJZAyZpaUwdDepd&index=10

https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.


"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def height_of_tree(root, is_balanced):
    if root == None:
        return 0

    left_height = height_of_tree(root.left, is_balanced)
    right_height = height_of_tree(root.right, is_balanced)

    if abs(left_height - right_height) > 1:
        is_balanced[0] = False

    return 1 + max(left_height, right_height)

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    is_balanced = [True]
    result = height_of_tree(root, is_balanced)
    print(result.is_balanced[0])

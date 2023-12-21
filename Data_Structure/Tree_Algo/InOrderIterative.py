"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Iterative inorder traversal

Take the stack.
1: keep adding all the left nodes to stack.
   update the node to node.left
2: When node.left is null.
   Pop the node.
   Assign root to root.right
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
"""
# Example usage:
# Construct a sample binary tree:   1
#                                  /   \
#                                 2     3
#                                / \
#                               4   5
"""
def inorderTraversal(root):
    # Add all the elements after traversal
    result = []
    stack = []

    while stack or root:
        # When root is not not null
        if root:
            stack.append(root)
            root = root.left
        else:
            # Pop the element
            node = stack.pop()
            result.append(node.val)
            root = node.right
    return result



    # while stack or root:
    #     while root:
    #         # Keep adding all the nodes to stack
    #         stack.append(root)
    #         root = root.left
    #     # Now the root becomes to None
    #     # Pop the  element
    #     node = stack.pop()
    #     result.append(node.val)
    #     # Move to the right tree
    #     if root and root.right:
    #         root = root.right
    #
    # return result

if __name__ == "__main__":
    # Example usage (using the same binary tree as before):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = inorderTraversal(root)
    print(result)







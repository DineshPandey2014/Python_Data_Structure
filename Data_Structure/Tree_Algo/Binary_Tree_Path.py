"""
https://leetcode.com/problems/binary-tree-paths/description/

Given the root of a binary tree, return all
root-to-leaf paths in any order.
A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"Not here we are passing path as pass by value"
"At every level each node has it's own String copy"
"1,2,3"
"1,2"
"1"
"1,3"

def binary_tree_path_pass_by_value(root, final_result, path):
    if root is None:
        return
    # Note converting every vlaue to string as str
    path = path + str(root.val)

    if root.left == None and root.right == None:
        final_result.append(path)

    binary_tree_path_pass_by_value(root.left, final_result, path + "->")
    binary_tree_path_pass_by_value(root.right, final_result, path + "->")


# result = []
# dfs(root, [], result)
# return result

def binary_tree_path_pass_by_reference(root, result, path):
    if root == None:
        return

    path.append(root.val)

    if root.left == None and root.right == None:
        result.append(path.copy())

    binary_tree_path_pass_by_reference(root.left,  result, path)
    binary_tree_path_pass_by_reference(root.right,  result, path)
    path.pop()


if __name__ == "__main__":
    # Example usage:
    # Assuming you have a binary tree defined as follows:
    #      1
    #     / \
    #    2   3
    #     \
    #      5

    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    # final_path = []
    # path = ""
    # binary_tree_path_pass_by_value(root, final_path, path)
    # print(final_path)

    final_path = []
    path = []
    binary_tree_path_pass_by_reference(root, final_path, path)
    print(final_path)


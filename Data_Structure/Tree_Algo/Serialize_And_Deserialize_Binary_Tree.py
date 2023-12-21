"""
Serialization is the process of converting a data structure or object into a sequence of bits so
that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary
tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different
approaches yourself.

Example 1:
     1
   /    \
2       3
     /     \
    4       5

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/

Serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with
different approaches yourself.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def dfs_seralize(root, result):
    if root == None:
        result.append("N")
        return
    # Converted int to str
    # Final return is String
    # In the result list it containd String
    data = str(root.val)
    result.append(data)
    dfs_seralize(root.left, result)
    dfs_seralize(root.right, result)

if __name__ == "__main__":
    result = []
    #dfs_seralize(root, result)
    print("".join(result))


def dfs_deserialize(data_list, index):
    token = data_list[index[0]]
    if token == "N":
        return None
    # Here token is in str need to convert to int
    node = TreeNode(int(token))
    index[0] = index[0] + 1
    node.left = dfs_deserialize(data_list, index)
    index[0] = index[0] + 1
    node.right = dfs_deserialize(data_list, index)
    return node

    input_list = data.split(",")
    index = [0]
    return dfs_deserialize(input_list, index)

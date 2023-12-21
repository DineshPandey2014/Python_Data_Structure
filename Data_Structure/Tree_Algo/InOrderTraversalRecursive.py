class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(node):
    if node == None:
        return

    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)
    return

if __name__ == "__main__":
    node_5 = TreeNode(5, None, None)
    node_2 = TreeNode(2, None, node_5)
    node_6 = TreeNode(6, None, None)
    node_3 = TreeNode(3, node_6, None)

    node_8 = TreeNode(8, None, None)
    node_7 = TreeNode(7, None, None)

    node_4 = TreeNode(4, node_7, node_8)

    node_1 = TreeNode(1, node_3, node_4)
    node_0 = TreeNode(0, node_1, node_2)
    inorder_traversal(node_0)



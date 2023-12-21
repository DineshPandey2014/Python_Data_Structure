class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
Did preorder traversing keep adding 1 for each node.
Base condition when 
"""
def countNode(node, count):
    if node == None:
        return
    # here we already counted root node as we did preorder traversing
    count[0] = count[0] + 1
    countNode(node.left, count)
    countNode(node.right, count)


if __name__ == "__main__":
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    node.left.left = TreeNode(0)
    node.right.right = TreeNode(5)
    result = [0]
    countNode(node, result)
    print(result[0])



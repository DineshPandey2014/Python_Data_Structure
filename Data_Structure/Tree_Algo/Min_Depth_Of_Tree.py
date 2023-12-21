class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



def minDepth(root) -> int:
    if root == None:
        return 0

    leftDepth = minDepth(root.left) + 1
    rightDepth = minDepth(root.right) + 1

    return min(leftDepth, rightDepth) + 1

if __name__ == "__main__":
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    depth = minDepth(root)
    print(depth)


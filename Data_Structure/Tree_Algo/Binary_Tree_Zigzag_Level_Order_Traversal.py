class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    if not root:
        return []
    result = []
    queue = [root]
    reverse = False
    while queue:
        level = []
        level_size =len(queue)

        for index in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # This is stack pop the elements from the last. Instead of reverse
        if reverse:
            level.reverse()
        reverse = not reverse
        result.append(level)
    return result

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    result = zigzagLevelOrder(root)
    print(result)





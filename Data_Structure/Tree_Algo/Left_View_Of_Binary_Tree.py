class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def LeftView(root):
    "Do level order traversal"
    "Use queue pop only first elements"

    ## Important if root == None return empty list
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        length = len(queue)
        ## Important in the result add first element
        leftnode = queue[0]
        result.append(leftnode.data)
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #        /
    #       7
    #
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(7)
    #root.left.left = TreeNode(4)
    result = LeftView(root)
    print(result)


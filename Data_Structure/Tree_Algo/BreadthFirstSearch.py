class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_tree(root):
    """Performs a breadth-first search of the given tree, starting at the given root node.

    Args:
      root: The root node of the tree.

    Returns:
      A list of the nodes visited in BFS order.
    """

    if not root:
        return
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print(current_node.val)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

# Example usage:
# Constructing a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("BFS traversal for the tree:")
    bfs_tree(root)



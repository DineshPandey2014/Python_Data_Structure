"""
 Here we keep traversing the nodes as PreOrder Traversal
 1: root is 0
 2: Left side vertical distance decrement by 1
 3: Right side vertical distance increment by1
 4: Will take a dictionary => Key will be vertical level
    To get a bottom view. We keep overriding the value to hash map.
 5: Sort the keys.
 7: Fetch the values for each vertical level there will be one value
 8: Return as array.
 """
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def bottom_view_of_binary_tree(root):
    if root is None:
        return []

    queue = [(root, 0)]
    result = []
    dict = {}
    while queue:
        node, ver_level = queue.pop(0)

        # Keep overriding the value
        dict[ver_level] = node.val

        if node.left:
            queue.append((node.left, ver_level - 1))

        if node.right:
            queue.append((node.right, ver_level + 1))

    result = [dict[key] for key in sorted(dict.keys())]

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

    result = bottom_view_of_binary_tree(root)
    print(result)


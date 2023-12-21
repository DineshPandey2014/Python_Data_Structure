class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def vertical_order_traverse(root):
    if root is None:
        return []
    # Keep a tupple
    queue = [(root, 0)]
    # Take a dict keys as level and values as node val
    dict = {}
    min_level = 0
    max_level = 0
    while queue:
        node, level = queue.pop(0)
        # Store the level as key in the dict
        # Store the value of node data which is val
        if level not in dict:
            if level < 0:
                min_level = min(min_level, level)
            if level > 0:
                max_level = max(max_level, level)
            level_data = []
            level_data.append(node.val)
            dict[level] = level_data
        else:
            dict[level].append(node.val)

        if node.left:
            queue.append((node.left, level - 1))

        if node.right:
            queue.append((node.right, level + 1))
    return dict, min_level, max_level

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

    result = vertical_order_traverse(root)
    print(result)

    result_dict, min_level, max_level = vertical_order_traverse(root)
    result = [result_dict[level] for level in range(min_level, max_level + 1)]
    print (result)
    # It print the result as expected  => [[4], [2], [1, 5, 6], [3], [7]]
    # Here node 5 and 6 has same vertical distance. So it come in the order of level order traversale
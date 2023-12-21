class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

"""
Modified the queue to store tuples of (node, level) for better handling of node and level information.

Used queue.pop(0) to simulate a queue (FIFO).

Changed root.data to node.data inside the loop.

Replaced fetch_top_view(root.left, level-1) and fetch_top_view(root.right, level+1) 
with queue.append((node.left, level - 1)) and queue.append((node.right, level + 1)), respectively.

Simplified the result generation using a list comprehension.
"""

def fetch_top_view(root):
    if root == None:
        return []
    queue = [(root, 0)]
    view_dict = {}
    while queue:
        node, level = queue.pop(0)
        # Fot top view will add only elements to view_dict if they don't present
        if level not in view_dict:
            view_dict[level] = node.data
        if node.left:
            queue.append((node.left, level - 1))
        if node.right:
            queue.append((node.right, level + 1))
    lowest_level = min(view_dict)
    highest_level = max(view_dict)
    result = [view_dict[key] for key in range(lowest_level, highest_level + 1)]
    return result

if __name__ == "__main__":
    # Example usage:
    # Construct a binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = fetch_top_view(root)
    print(result)  # Output should be [4, 2, 1, 3]

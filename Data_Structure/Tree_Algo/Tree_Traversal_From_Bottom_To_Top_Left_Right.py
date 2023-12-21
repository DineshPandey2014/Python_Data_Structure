"""
Level order traversal from bottom to top.

# Example usage:
# Construct a binary search tree
#       2
#      / \
#     1   3
     /     \
    0       5
tree_root = TreeNode(2)
tree_root.left = TreeNode(1)
tree_root.right = TreeNode(3)

Answer => 0 , 5, 1 , 3, 2

Add all the elements in the queue.
1) Traverse right to Left
2) Pop the element from queue add to stack
3) Print the stack
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse_from_bottom_top(node):
    stack = []
    """
    Here we add the root element first in the stack.
    And then add right element and then left element
    Pop from the stack
    
    Add the elements to stack.
    Pop the element from the stack
    1) Add element 2 to stack
     [2]
    2) Add element 3 to stack
    [3,1]
    3) Add element 1 to stack
    [2, 3, 1]
    4) Add element 5 to stack
    [2, 3,1, 5]
    5) 4) Add element 0 to stack
    [2, 3,1, 5, 0]
    """
    result_stack = []
    # Here queue holding the nodes from right and then left
    # Fetch from index 0 of the queue

    queue = [node]
    while queue:
        node = queue.pop(0)
        # Add first right element
        result_stack.append(node.val)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

    # print the stck

    while result_stack:
        print(result_stack.pop())


if __name__ == "__main__":
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    node.left.left = TreeNode(0)
    node.right.right = TreeNode(5)
    traverse_from_bottom_top(node)




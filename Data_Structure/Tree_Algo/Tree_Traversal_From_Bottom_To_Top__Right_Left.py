"""
Add all the elements in the queue.
1) Traverse Left to Right
2) Pop the element from queue add to stack
3) Print the stack

#       2
#      / \
#     1   3
     /     \
    0       5

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse_from_bottom_top(node):
    queue = [node]
    result_stack = []
    while queue:
        # For queue pop the element form the front index 0
        node = queue.pop(0)
        result_stack.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # For stack pop the element from the last of the list
    while result_stack:
        value = result_stack.pop()
        print(value)

if __name__ == "__main__":
    node = TreeNode(2)
    node.left = TreeNode(1)
    node.right = TreeNode(3)
    node.left.left = TreeNode(0)
    node.right.right = TreeNode(5)
    traverse_from_bottom_top(node)






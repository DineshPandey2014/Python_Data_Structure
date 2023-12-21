"""
Given a full binary expression tree consisting of basic binary operators (+, -,*, /) and some integers,
Your task is to evaluate the expression tree.

Input:
              +
           /     \
          *       -
        /  \    /   \
       5    4  100  20

Output: 100

Explanation:
((5 * 4) + (100 - 20)) = 100

Here first we converted postfix expression to Tree.
And then we  traverse the tree as inorder
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def evalTree(root):
    # Code here
    # Here we have operand is at the leave node. When root.left is None and root.right is Noen
    if root.left == None and root.right == None:
        return int(root.data)

    left_data = evalTree(root.left)
    right_data = evalTree(root.right)

    if root.data == "+":
        return left_data + right_data
    elif root.data == "-":
        return left_data - right_data
    elif root.data == "*":
        return left_data * right_data
    else:
        return left_data / right_data

if __name__ == "__main__":
    # Constructing the expression tree: (+ ( * (5) (4) ) ( - (100) (20) ) )
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('20')

    # Expected result: (5 * 4) + (100 - 20) = 20 + 80 = 100
    expected_result = 100

    # Evaluate the expression tree
    result = evalTree(root)

    print("result: ",result)
    # Test the result against the expected result
    print("Test Passed:", result == expected_result)
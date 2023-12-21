class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def constructTree(postfix):
    stack = []

    for char in postfix:
        node = Node(char)
        if char.isalnum():  # Check if the character is an operand
            stack.append(node)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            node.left, node.right = operand1, operand2
            stack.append(node)

    return stack[0]

def infix_traversal(root, result):
    if root == None:
        return
    infix_traversal(root.left, result)
    result.append(root.value)
    infix_traversal(root.right, result)

# Post order traversal is LEFT RIGHT NODE traversal
"ab+c*"
def build_tree_from_postfix_recursive(prefix_notation, index):
    token = prefix_notation[index[0]]
    node = Node(token)
    if token in ["+", "-", "*", "/"]:
        index[0] = index[0] - 1
        node.right = build_tree_from_postfix_recursive(prefix_notation, index)
        index[0] = index[0] - 1
        node.left = build_tree_from_postfix_recursive(prefix_notation, index)
    return node





# def infixExpression(root):
#     if root:
#         if root.value.isalnum():  # Check if the value is an operand
#             return root.value
#         else:
#             return f"({infixExpression(root.left)} {root.value} {infixExpression(root.right)})"

if __name__ == "__main__":
# Example usage:
    postfixExpression = "ab+c*"
    result = []
    # infixResult = constructTree(postfixExpression)
    length_of_prefix_notation = len(postfixExpression)
    index = [length_of_prefix_notation -1]
    postfix_tree = build_tree_from_postfix_recursive(postfixExpression, index)
    print(postfix_tree)
    infix_traversal(postfix_tree, result)
    print("Infix Expression:", "".join(result))
    #infix_traversal(infixResult, result)
    #print("Infix Expression:", "".join(result))
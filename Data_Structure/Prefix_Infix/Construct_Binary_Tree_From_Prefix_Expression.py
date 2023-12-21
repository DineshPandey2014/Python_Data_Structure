"""
Input: a[] = “*+ab-cd”
Output: The Infix expression is:
a + b * c – d

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#  prefix_expression = "+*ab-cd"
def build_tree_from_prefix_recursive(prefix_expression, index):
    token = prefix_expression[index[0]]
    node = Node(token)
    if token in ("+", "-" , "/" , "*"):
        index[0] = index[0] + 1
        node.left = build_tree_from_prefix_recursive(prefix_expression, index)
        index[0] = index[0] + 1
        node.right = build_tree_from_prefix_recursive(prefix_expression, index)
    return node

# Prefix notation is  preorder traversal
def print_prefix(root, result):
    if root == None:
        return
    result.append(root.value)
    print_prefix(root.left, result)
    print_prefix(root.right, result)


def is_operator(token):
    return token in '+', '-', '*', '/'

if __name__ == "__main__":
    prefix_expression = "+*ab-cd"
    index = [0]
    expression_tree_root = build_tree_from_prefix_recursive(prefix_expression, index)
    result = []
    print_prefix(expression_tree_root, result)
    print("".join(result))


def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    """
    https://www.youtube.com/watch?v=Rezetez59Nk

    1) Here we will find the height of Tree in every subtree.
    2) Hold the max which will be diameter in every node
       max_diameter = (max_diameter, left_height + right_height)
    """
    max_diameter = 0
    def find_diameter(root):
        # nonlocal keyword to tell Python that you are referring to the global variable max_diameter:
        nonlocal max_diameter
        if root == None:
            return 0

        left_height = find_diameter(root.left)
        right_height = find_diameter(root.right)

        # Here we are not adding 1 to =>  left_height + right_height
        # It's already added when the height of the node is return which
        # max of left height and right height
        max_diameter = max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    find_diameter(root)
    return max_diameter
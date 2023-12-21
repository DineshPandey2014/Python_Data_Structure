class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_Tree(p, q):
    if p == None and q == None:
        return True

    if p == None or q == None:
        return False

    if p.val != q.val:
        return False

    return is_same_Tree(p.left, q.left) and is_same_Tree(p.right, q.right)

"""
Will do level order traversal travers each node put in the queue
Pop the node from the queue. Check if the val is mathicg with subroot.
It means we can check for same tree
"""

def is_subTree_Check(root, subRoot):
    if root == None:
        return False

    queue = [root]
    while queue:
        node = queue.pop(0)

        if node.val == subRoot.val:
            return is_same_Tree(node, subRoot)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    # We traverse entire tree not finding any match
    return False

if __name__ == "__main__":
    # Define the main tree
    main_tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))

    # Define the subtree
    subtree = TreeNode(4, TreeNode(1), TreeNode(2))

    # Instantiate the Solution class
    # solution = Solution()
    #
    # # Test the isSubtree function
    # result = solution.isSubtree(main_tree, subtree)
    #
    # # Expected output: True, as the subtree is present in the main tree
    # print("Test Passed:", result)
    # return is_subTree_Check(root, subRoot)

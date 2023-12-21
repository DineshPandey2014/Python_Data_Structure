class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxval = float('-inf')
        count = 0

        def dfs(root, maxvalue):
            if root is None:
                return 0

            # Check if the current node is a "good" node
            if root.val >= maxvalue:
                ans[0] += 1
                maxvalue = root.val

            # Explore both left and right subtrees
            dfs(root.left, maxvalue)
            dfs(root.right, maxvalue)

            #return left_count + right_count

        ans = [0]  # Using a list to store count as integers are immutable
        dfs(root, float('-inf'))
        return ans[0]


if __name__ == "__main__":
    # Example usage:
    # Constructing a sample binary tree
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    1   8     7
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.goodNodes(root)
    print("Number of good nodes in the binary tree:", result)
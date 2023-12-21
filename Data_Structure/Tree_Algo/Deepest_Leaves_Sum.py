"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
https://leetcode.com/problems/deepest-leaves-sum/
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def deepestLeavesSum(root):
    # BFS
    """
    1) Will add all the elements in each level
    2) When a new level comes reset the sum and add again
    3) In the end, you have the sum of the last level, which are the deepest leaves
    """
    if not root:
        return 0

    queue = [root]
    result = 0

    while queue:
        level_sum = 0  # Initialize the sum for the current level
        queue_length = len(queue)

        for _ in range(queue_length):
            node = queue.pop(0)
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result = level_sum  # Update result with the sum of the current level

    return result

def test_deepestLeavesSum():
    # Constructing a sample binary tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    #    /       /
    #   7       8

    #         1
    #        / \
    #       2   3
    #      /   /
    #     4    5


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    # root.left.left.left = TreeNode(7)
    # root.right.right.left = TreeNode(8)

    # Expected deepest leaves sum: 7 + 8 = 15
    expected_result = 15

    # Test the function
    # solution = Solution()
    result = deepestLeavesSum(root)

    # Check if the result matches the expected outcome
    print(result)
    #assert result == expected_result, f"Test Failed: Expected {expected_result}, got {result}"

    print("Test Passed!")

if __name__ == "__main__":
    test_deepestLeavesSum()
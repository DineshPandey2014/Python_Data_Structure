"""
https://leetcode.com/problems/range-sum-of-bst/

Algorithm :
Here we need to add all the elements which are in the range of low and high
1 : Here we are passing the list whose with index 0. Default vaule is zero
2: When you reach to the leaf nodes. When root is None will return.
3: Here we need to traverse a tree. 
4: We did preorder traversal. Check the condition of low and high with root.val
5: Just did In order traversal
6: Store the result
7: Return the result
"""


def rangeSumBST(root, low: int, high: int):
    result = [0]

    def rangeSum(root, low, high, result):
        if not root:
            return

        if root.val >= low and root.val <= high:
            result[0] = result[0] + root.val

        rangeSum(root.left, low, high, result)
        rangeSum(root.right, low, high, result)

    rangeSum(root, low, high, result)
    return result[0]
"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""


def largestValues(root):
    # BFS
    if root == None:
        return []

    result = []
    queue = [root]

    while queue:
        length_of_queue = len(queue)
        max_element_in_each_row = float(-inf)
        for index in range(length_of_queue):
            # Here we need to pop the element from the queue.
            # Inside for loop we need to pop all the elements which are in the same level.
            node = queue.pop(0)

            if node.val > max_element_in_each_row:
                max_element_in_each_row = node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        result.append(max_element_in_each_row)
    return result


def largestValues_version_2(root):
    # BFS
    if root == None:
        return []

    result = []
    queue = [root]

    while queue:
        length_of_queue = len(queue)
        temp = []
        for index in range(length_of_queue):
            # Here we need to pop the element from the queue.
            # Inside for loop we need to pop all the elements which are in the same level.
            node = queue.pop(0)
            temp.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        result.append(max(temp))
    return result
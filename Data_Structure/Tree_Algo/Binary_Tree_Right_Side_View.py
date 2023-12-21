"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

https://leetcode.com/problems/binary-tree-right-side-view/
"""

"""
Algo : Take a queue as list
1) Add the node in the queue of each level
2) Here we need to look the right view. Add the last element from the queue to the result
3) Inside the for loop which ran size of the queue. This loop runs size of the queue
4) Here we pop all the elements belongs to each level.
5) Add all the elements next level in the queue.

Conclusion: After this loop we have the last element which will be part of the right side view.
   
"""

def rightSideView(root):
    # Use BFS Row level traversal
    if root is None:
        return []

    queue = [root]
    right_side_view = []
    while queue:
        length_of_each_row_element = len(queue)
        right_side_view.append(queue[-1].val)
        for index in range(length_of_each_row_element):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return right_side_view
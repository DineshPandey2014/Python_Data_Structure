"""
Given a Binary Tree of size N and an integer K. Print all nodes that are at distance k
from root (root is considered at distance 0 from itself). Nodes should be printed from left to
right. If k is more that height of tree, nothing should be printed.
"""



def k_distance_node(root, k, result, current_distance):
    if root == None:
        return

    if current_distance == k:
        result.append(root.data)
        return
    # Here we store each level distance
    k_distance_node(root.left, k, result, current_distance + 1)
    k_distance_node(root.right, k, result, current_distance + 1)


    result = []
    current_distance = 0
    # k level is starting form 0
    k_distance_node(root, k, result, current_distance)
    return result

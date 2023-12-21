"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

"""



def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Algo : To find the lowest common ancestor in the BST.
    1) Case 1=> Need to check if p and q are left side of Tree go left side.
    2) Case 2=> If p and q are right side of Tree go right side of Tree.
    3) Case 3=> In this case root is the LCA means where we have split of the node of P and Q

    Example: Let's say P os 0 node and q is 2 node.
    Case 3=> P and Q are the right side it means LCA is 2
    return 2
    """
    if root is None:
        return None
    # left
    if p.val < root.val and q.val < root.val:
        # Here we are returning back as we get the return when this condition not satisfied
        return self.lowestCommonAncestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    # Now here we are at the lowest node which is LCA
    else:
        # Here we are returning the node which is LCA for p and q node
        return root


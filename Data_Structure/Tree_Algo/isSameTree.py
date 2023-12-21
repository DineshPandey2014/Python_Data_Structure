# Use depth search traversal.
class Tree:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class TrreAlgo:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        # Compare the right tree with right tree
        # Compare the left tree with left tree
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)















"""
DFS traversal
1) Checks if Node is None return
2) Go to left
"""


def dfs(self, node):
    if node == None:
        return
    dfs(node.left)
    dfs(node.right)
    return




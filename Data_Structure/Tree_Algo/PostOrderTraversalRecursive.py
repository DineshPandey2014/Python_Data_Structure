def post_order_dfs(node):
    if node == None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.val)
    return
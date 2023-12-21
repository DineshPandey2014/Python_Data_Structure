"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

You have a graph of n nodes. You are given an integer n and an array edges where
edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.


"""

from collections import defaultdict

def countComponents(n, edges) -> int:
    # Create the graph. It's undirected graph have edge both side
    # A ---> B
    # B ---> A
    edge_dict = defaultdict(list)
    for a, b in edges:
        edge_dict[a].append(b)
        edge_dict[b].append(a)
    visited = set()

    # Here in dfs we traverse all the connected nodes of n. Means direct
    # and indirect neighbour
    def dfs_find_comp(node):
        visited.add(node)
        for neighbour in edge_dict[node]:
            if neighbour not in visited:
                dfs_find_comp(neighbour)

    components = 0

    # Here node start with 0,1,2,3...n
    # if n = 4. ( loop goes from 0 to 3)
    # find all the connected nodes of n which are direct and indirect
    for node in range(n):
        # will call dfs only when the node is not visited
        # once all the connected nodes traversed will count the components as one
        # Then in the for loop go to next node checked if not visited then only call the dfs
        # if not traversed.
        if node not in visited:
            dfs_find_comp(node)
            # once we traverse all the node which are direct and  indirect neighbur
            # We can increment count of component
            components = components + 1
    return components

if __name__ == "__main__":
    n = 5
    edges = [(0, 1), (1, 2), (3, 4)]
    result = countComponents(n, edges)
    print("Number of Connected Components:", result)
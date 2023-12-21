"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1
(inclusive). The edges in the graph are represented as a 2D integer array edges, where each
edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair
 is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from
source to destination, or false otherwise.

"""
from collections import defaultdict

def validPath(n:int , edges:int, source: int, destination: int) -> bool:
    dict_edge = defaultdict(list)
    for a, b in edges:
        dict_edge[a].append(b)
        dict_edge[b].append(a)
    seen = [False] * n

    def dfs_path(curr_node):
        if curr_node == destination:
            return True

        if not seen[curr_node]:
            seen[curr_node] = True
            for next_node in dict_edge[curr_node]:
                if dfs_path(next_node):
                    return True
        return False
    return dfs_path(source)

if __name__ == "__main__":
    # n = 3
    # edges = [[0, 1], [1, 2], [2, 0]]
    # source = 0
    # destination = 2

    n = 6
    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source = 0
    destination = 5
    result = validPath(n, edges, source, destination)
    print(result)
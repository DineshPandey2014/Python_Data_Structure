"""
797. All Paths From Source to Target


https://leetcode.com/problems/all-paths-from-source-to-target/description/

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths
from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).

"""


def all_paths_dfs(graph, node, path, result):
    if node == n - 1:
        result.append(path.copy())  # Copy the current path before appending to the result
        return

    for neighbor in graph[node]:
        path.append(neighbor)
        all_paths_dfs(graph, neighbor, path, result)
        path.pop()  # Backtrack by removing the last node from the path

# result = []
# n = len(graph)
# dfs(0, [0])
# return result

if __name__ == "__main__":
    result = []
    graph = [[1, 2], [3], [3], []]
    n = len(graph)
    # Input parameter
    # graph
    # Starting node 0
    # Path as list. Will pop as recursive algo
    # result append when the length of path is same to length of graph -1
    # In the result will copy
    paths = all_paths_dfs(graph, 0, [0], result) # graph, node, Add 0 to result as path start from 0
    print(result)
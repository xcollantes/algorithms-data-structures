"""
Depth first search.

Known as Depth First Traversal, is the recursive algorithm to visit each node in
a graph or tree structure.

Time complexity is O(Nodes + Edges).

Space complexity is O(Nodes).

The purpose is to reach as far as the graph can go, hence "depth" as opposed to
Breadth First Search which iterates nodes in a graph nearest to the starting
point first.

More info: depth_first_search/README.md
"""

import logging
from collections import deque


def recursive_dfs(visited: deque, graph: dict, node: any) -> list:
    """Traversal of all nodes in graph using DFS using recursion.

    1. Start at a node
    2. Push all the adjacent nodes on stack
    3. Perform action on node
       (The operation is simply print the value of the node.)
    4. Push current node to "visited" stack
    5. Move next to top of adjacent stack
    6. Go to 1; stop when the adjacent stack is empty

    Args:
        visited: Stack of nodes we have visited.
        graph: Entire graph.
        node: Content of current node.
    """
    if node not in visited:
        logging.info("RECURSION: Visiting node: %s", node)
        visited.append(node)

        for adjacent_node in graph[node]:
            recursive_dfs(visited, graph, adjacent_node)

    return visited


def dfs_stack(graph: dict, start_node: any) -> list:
    """Traverse all nodes in graph using DFS with iterating over nodes."""
    visited: list[any] = []
    stack: list[any] = [start_node]

    while stack:
        node: any = stack.pop()
        if node not in visited:
            logging.info("STACK: Visiting node: %s", node)
            visited.append(node)

            for adjacent_node in graph[node]:
                stack.append(adjacent_node)

    return visited

"""Breadth First Search or BFS.

Traverse graph structure by reaching each node. This search algorithm is similar
to DFS except BFS will check the sibling nodes first as opposed to traversing
the entire length of child nodes first.

Newly visited nodes must be kept track so you don't visit a node more than once.
Keep track using a queue where you push a visited node onto the queue then pop a
node off the queue if you have no adjacent nodes to visit.

Time complexity: O(Vertices + Edges)

Process:
"""

from collections import deque
import logging


def bfs(graph: dict, start_node: any) -> set:
    """BFS."""
    # Keep only one instance of each node since the same node must be visited
    # more than once but not tracked.
    visited: set = set()
    adjacent_stack: deque = deque([start_node])
    while adjacent_stack:

        # Visit the "nearest" neighbor first or left-most node on adjacent_stack
        current_node = adjacent_stack.popleft()
        logging.info("BFS: Visiting node: %s", current_node)
        visited.add(current_node)

        # Make sure neighbor nodes are not visited to prevent loop
        for node in graph[current_node]:
            if node not in visited:
                adjacent_stack.append(node)

    return visited
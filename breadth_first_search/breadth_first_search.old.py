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

import logging


def bfs(graph: dict, root: any):
    """BFS with predefined Python queue.

    Args:
        graph: Entire graph.  root: First element in graph.
    """
    from collections import deque

    logging.info("Breadth First Search")

    visited: dict(Any, bool) = {n: False for n in graph}

    adjacent_queue: deque = deque()
    adjacent_queue.append(root)

    while adjacent_queue:

        logging.info("Popping head %s from %s", adjacent_queue[0], adjacent_queue)
        node: Any = adjacent_queue.popleft()

        visited[node] = True
        logging.info("Visiting node: %s", node)

        for adjacent_node in graph[node]:
            logging.info("Adjacent node: %s", adjacent_node)

            # In this case, we make sure the adjacent nodes are not already
            # visited nor are adjacent nodes already in queue.  Making sure
            # adjacent nodes are not in adjacent queue means duplicate values
            # are not allowed or are treated as the same node.
            if not visited[adjacent_node] and adjacent_node not in adjacent_queue:
                adjacent_queue.append(adjacent_node)


def bfs_iterative(graph: dict, root: Any):
    """BFS solved iteratively using native List used for queue.

    Args:
        See bfs().
    """
    logging.info("Breadth First Search, iterative")

    visited: dict[any, bool] = {n: False for n in graph}
    logging.info("Visited dict: %s", visited)

    adjacent_queue: list = [root]  # Initialize with first node

    while adjacent_queue:

        logging.info("Popping head: %s from %s", adjacent_queue[0], adjacent_queue)
        node: any = adjacent_queue[0]
        del adjacent_queue[0]

        logging.info("Visiting node: %s", node)
        visited[node] = True

        for adjacent_node in graph[node]:
            logging.debug("Adjacent node: %s", adjacent_node)

            # Checks for
            #  1. Adjacent node is not visited
            #  2. Adjacent node is not already in Adjacent queue These cases can
            # occur where two upstream nodes point to the same node.  Do not
            # count the downstream node twice.
            if not visited[adjacent_node] and adjacent_node not in adjacent_queue:
                adjacent_queue.append(adjacent_node)

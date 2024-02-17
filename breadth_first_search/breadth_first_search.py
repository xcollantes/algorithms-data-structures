"""Breadth First Search or BFS. 

Traverse graph structure by reaching each node.  This search algorithm is 
similar to DFS except BFS will check the sibling nodes first as opposed to 
traversing the entire length of child nodes first.  

Newly visited nodes must be kept track so you don't visit a node more than
once.  Keep track using a queue where you push a visited node onto the
queue then pop a node off the queue if you have no adjecent nodes
to visit.  The pop action is a backtrack to search other nodes.

If you want to find the shortest path in a graph, then BFS is preferred.  For
example, if using DFS, you'd have to traverse the length of the tree even
two nodes are near each other horizontally.

# Depth First vs Breadth First

There are two methods to traverse a graph data structure:
    - Depth First Search
    - Breadth First Search

Both will work with the same result to traverse a graph structure but a Depth
First Search is simpler if you want to visit every node in the tree.

Tracking max length: To find the longest length, BFS can keep track of this 
internally where DFS must keep track with a global map since DFS is recursive. 

Time complexity: O(Vertices + Edges)

Process: 
"""

import logging
from typing import Any

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


def main():
    # Graph is undirected since e refers back to 1, 2, and 3.
    #
    #    0
    #  / | \
    # 1  2  3
    #  \ | /
    #    4
    graph: dict(int, int) = {
        0: [1, 2, 3],
        1: [4],
        2: [4],
        3: [4],
        4: [1, 2, 3]
    }

    import pdb
    bfs(graph, 0)
    # bfs_iterative(graph, 0)


def bfs(graph: dict, root: Any):
    """BFS with predefined Python queue.

    Args:
        graph: Entire graph. 
        root: First element in graph.
    """
    from collections import deque

    logging.info("Breadth First Search")

    visited: dict(Any, bool) = {n: False for n in graph}

    adjacent_queue: deque = deque()
    adjacent_queue.append(root)

    while adjacent_queue:

        logging.info("Popping head %s from %s",
                     adjacent_queue[0], adjacent_queue)
        node: Any = adjacent_queue.popleft()

        visited[node] = True
        logging.info("Visiting node: %s", node)

        for adjacent_node in graph[node]:
            logging.info("Adjacent node: %s", adjacent_node)

            # In this case, we make sure the adjacent nodes are not
            # already visited nor are adjacent nodes already in queue.
            # Making sure adjacent nodes are not in adjacent queue means
            # duplicate values are not allowed or are treated as the same node.
            if not visited[adjacent_node] and adjacent_node not in adjacent_queue:
                adjacent_queue.append(adjacent_node)


def bfs_iterative(graph: dict, root: Any):
    """BFS solved iteratively using native List used for queue.

    Args: 
        See bfs(). 
    """
    logging.info("Breadth First Search, iterative")

    visited: dict(Any, bool) = {n: False for n in graph}
    logging.info("Visited dict: %s", visited)

    adjacent_queue: list = [root]  # Initialize with first node

    while adjacent_queue:

        logging.info("Popping head: %s from %s",
                     adjacent_queue[0], adjacent_queue)
        node: Any = adjacent_queue[0]
        del adjacent_queue[0]

        logging.info("Visiting node: %s", node)
        visited[node] = True

        for adjacent_node in graph[node]:
            logging.debug("Adjacent node: %s", adjacent_node)

            # Checks for
            #  1. Adjacent node is not visited
            #  2. Adjacent node is not already in Adjacent queue
            # These cases can occur where two upstream nodes point to the same
            # node.  Do not count the downstream node twice.
            if not visited[adjacent_node] and adjacent_node not in adjacent_queue:
                adjacent_queue.append(adjacent_node)


if __name__ == "__main__":
    main()

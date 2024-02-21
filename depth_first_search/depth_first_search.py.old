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
    graph: list(tuple(int, int)) = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 1),
        (4, 2),
        (4, 3),
    ]
    graph_two: dict(int, int) = {
        0: [1, 2, 3],
        1: [4],
        2: [4],
        3: [4],
        4: [1, 2, 3]
    }

    visited: dict(Any, bool) = {vertex: False for vertex in graph_two.keys()}

    logging.info("Visited tracker: %s", visited)
    logging.info("Graph: %s", graph_two)

    logging.info("DFS recursive")
    dfs_recursive(visited, graph_two, list(graph_two.keys())[0])

    logging.info("DFS iterative")


def dfs_recursive(visited: dict, graph: dict, node: Any):
    """Traverse the entire graph and print out values.

    Args:
        visited: Hash map of nodes and if we have visited it.
        graph: The entire graph.
        node: Current node.
    """
    if not visited[node]:
        logging.info("Visited new node: %s", node)
        visited[node] = True

        for adjacent_node in graph[node]:
            dfs_recursive(visited, graph, adjacent_node)


if __name__ == "__main__":
    main()

"""Infected node in network path.

Given a start node, stop node, and infected node, see if a path is possible.
"""

from collections import deque
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


# Input network is undirected.
NETWORK = {
    1: [2],
    2: [1, 4, 3],
    3: [2],
    4: [5],
    5: [6],
    6: [7],
    7: [8],
    8: [7, 9],
    9: [8, 11],
    10: [8, 12],
    11: [9, 12],
    12: [11, 10],
}


def main():
    assert path_exists(2, 9, 7) == False
    assert path_exists(1, 5, 7) == True


def path_exists(start: int, stop: int, infected: int) -> bool:
    """Determine if start and stop have a connection without infected node.

    Traverse the network as if we don't know the entire network.  

    Args: 
        start: Beginning point to trace path.
        stop: Finish point to trace path.
        infected: Node which cannot be passed.

    Returns:
        True if start and stop have a connection without infected Node.
        False if no path is found without infected node.  
    """
    if not NETWORK:
        return False
    if start is stop:
        return True

    visited = list()
    adj = deque([start])

    while len(adj) != 0:
        if (start and stop in visited) and (infected not in visited):
            return True
        elif (start in visited) and (stop not in visited) and (infected in visited):
            return False
        else:
            current = adj.pop()
            logging.info("Visiting: %s", current)
            visited.append(current)

            for child in NETWORK[current]:
                if child not in visited:
                    adj.append(child)
                    logging.debug("Children pushed on adj: %s", child)


if __name__ == "__main__":
    main()

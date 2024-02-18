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

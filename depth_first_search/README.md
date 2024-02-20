# Depth First Search or DFS

Recursive algorithm for traversing a graph structure by reaching each node until
the end is found then returning to the previously visited nodes until a new one
is visited.

Time complexity is O(V + E) where V is the number of vertices in a graph and E
is the number of edges.

## Depth First vs Breadth First

There are two methods to traverse a graph data structure:

- Depth First Search
- Breadth First Search

DFS comes in 3 variations:

- Pre-order
- In-order
- Post-order

Both will work with the same result to traverse a graph structure but a Depth
First Search is simpler if you want to visit every node in the tree.

If you want to find the shortest path in a graph, then BFS is preferred. For
example, if using DFS, you'd have to traverse the length of the tree even two
nodes are near each other horizontally.

DFS will travel down one direction until a node is found then backtrack.

The process is as follows for DFS:

1. Start at a node
2. Push all the adjacent nodes on stack
3. Perform action on node
4. Push current node to "visited" stack
5. Move next to top of adjacent stack
6. Go to 1; stop when the adjacent stack is empty

## Representation

To represent vertices, there are two options:

- Adjacency list: tuples of vertices and their connection. If Vertex A has an
  edge with Vertex B, then it would be represented with `(A,B)`. If the edge is
  not directed or the edge is two way, then there would be two tuples, `(A,B)`
  and `(B,A)`.

- Adjacency matrix: a table representation where the vertices are listed on the
  header and left side of the table and the values are true or false depending
  if there is an edge between the two vertices. This is less efficient compared
  to the list since you'd have to traverse the table N\*N times.

## Space complexity

From what I can research, there always needs to be 2 list type data structures
(lists, arrays, stacks). One list for tracking "visited" nodes and one list for
"to visit" nodes. Time complexity is O(Nodes) because the most space you can
track is the max number of nodes since a node is either visited, to visit, not
yet known.

## BFS vs DFS

Breadth First Search is good for prioritizing the sibling nodes which are the
same level as the starting point.

Depth First Search is good for reaching as far as the graph goes as a priority.

In both, each node will be checked.

On a technical practice, the biggest difference is that the data structure which
tracks the neighbors. In BFS the "next node" to check is taken from the left of
the queue. In DFS the "next node" to check is taken from the right. In both we
assume you are adding new nodes to the right of the queue.

## Use cases

Topological sorting, scheduling problems, graph cycle detection, and solving
puzzles with one solution such as traverse a maze or solve a sudoku puzzle all
require the use of DFS. Computer networking uses DFS for example if a network is
bipartite.

Sources:

- <https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm>
- <https://favtutor.com/blogs/depth-first-search-python>
- <https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial>

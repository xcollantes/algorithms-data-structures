# Depth First Search or DFS

Recursive algorithm for traversing a graph structure by
reaching each node until the end is found then returning to the previously
visited nodes until a new one is visited.

Time complexity is O(V + E) where V is the number of vertices in a
graph and E is the number of edges.

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

If you want to find the shortest path in a graph, then BFS is preferred.  For
example, if using DFS, you'd have to traverse the length of the tree even
two nodes are near each other horizontally.

DFS will travel down one direction until a leaf is found then backtrack.

![leetcode image](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/Figures/DSA/Chapter_5/25_1.png)

Given the graphic above, you would keep calling `node.left` until there is a
null, then call `node.right`.  

The process is as follows for DFS:

1. Handle the base case, usually empty tree.  
2. Do a thing to the data of hte current node.  
3. Recursively call all the children of the current node.  
4. Return the answer.  

Note: 2 and 3 changes order depending on in-order, pre-order, post-order.  

## Representation

To represent vertices, there are two options:

- Adjacency list: tuples of vertices and their connection.  If Vertex A
    has an edge with Vertex B, then it would be represented with `(A,B)`.  If
    the edge is not directed or the edge is two way, then there would be two
    tuples, `(A,B)` and `(B,A)`.

- Adjacency matrix: a table representation where the vertices are listed on
    the header and left side of the table and the values are true or false
    depending if there is an edge between the two vertices.  This is less
    efficient compared to the list since you'd have to traverse the table N*N
    times.

## Use cases

Topological sorting, scheduling problems, graph cycle detection,
and solving puzzles with one solution such as traverse a maze or
solve a sudoku puzzle all require the use of DFS.  Computer networking
uses DFS for example if a network is bipartite.

Sources:

- <https://www.simplilearn.com/tutorials/data-structure-tutorial/dfs-algorithm>
- <https://favtutor.com/blogs/depth-first-search-python>
- <https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial>

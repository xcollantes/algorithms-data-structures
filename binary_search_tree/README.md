# Binary tree

A tree where each node can possibly have up to 2 children.

Perfect binary tree: All nodes have 0 or 2 children and all leaf nodes are at
the same level.

Full binary tree: All nodes have 0 or 2 children.

Complete tree: Every level is filled, all leaf elements have 0, 1, or 2 children
but if a node has only one child, it's the left child.

Relationship between an array and trees: A complete binary tree can have its
children and parents with `2i + 1` to find the left child and `2i + 2` to find
the right child where `i` is the index of the array.

The parent can be found with the opposite: `(i - 1) / 2`.

![programwiz.com](https://cdn.programiz.com/cdn/farfuture/yBcZxf7VSecOV66J8-kdwS0lX5mah3oLZzWcbRNqFog/mtime:1586942656/sites/tutorial2program/files/array-vs-heap-indices.png)

## Tree structures

Tree: Collection of linked nodes. Use a tree to perform operations in more
efficient time complexity than linear data structures.

Forest: Collection of disjoint trees.

Node: A single leaf in the tree which contains a key or value and pointers to
the child nodes.

Edge: Link between two nodes.

Height of a Node: Number of edges from the node to the deepest leaf.

Leaf: Node of tree with no children.

![leetcode
image](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/Figures/DSA/Chapter_5/25_1.png)

Given the graphic above, you would keep calling `node.left` until there is a
null, then call `node.right`.

## n-nary tree

A tree where each node can possibly have 0 to infinitely many children.

## B-tree or Balanced tree

"""Data models for searching Leetcode library."""

from dataclasses import dataclass
from enum import Enum


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Tags(Enum):
    ARRAY = "array"
    BACKTRACKING = "backtracking"
    BFS = "bfs"
    BINARY_SEARCH = "binary search"
    BINARY_SEARCH_TREE = "binary search tree"
    BINARY_TREE = "binary tree"
    BIT_MANIPULATION = "bit manipulation"
    DESIGN = "design"
    DFS = "dfs"
    DYNAMIC_PROGRAMMING = "dynamic programming"
    GRAPH = "graph"
    HASH_TABLE = "hash table"
    HEAP = "heap"
    LINKED_LIST = "linked list"
    MATH = "math"
    MATRIX = "matrix"
    MAZE = "maze"
    MEMOIZATION = "memoization"
    QUEUE = "queue"
    RECURSION = "recursion"
    SLIDING_WINDOW = "sliding window"
    SORTING = "sorting"
    STACK = "stack"
    STRING = "string"
    TOP_K_ELEMENTS = "top k elements"
    TREE = "tree"
    TWO_POINTERS = "two pointers"
    XOR = "xor"


@dataclass
class Metadata:
    tags: list[Tags]
    difficulty: Difficulty
    source: str = "Leetcode"

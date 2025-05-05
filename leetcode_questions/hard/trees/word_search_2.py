"""212. Word Search II

Hard

Given an m x n board of characters and a list of strings words, return all words
on the board.

Each word must be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once in a word.

Example 1:

Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


def word_search_2(board, words) -> list[str]:
    """"""

    def dfs(x, y, root):

        print(f"calling DFS: {x} {y} {root}")

        # Current letter on board. For sure in our node since it is requirement
        # in the board[xo][yo] in cur_node.
        letter = board[x][y]

        # Get the current node which has the letter.
        cur_node = root[letter]

        # End of word check. Since the value of the "#" is end of word and word
        # is also the value.
        word = cur_node.pop("#", False)
        print(f"base case: {word}")
        if word:
            result.append(word)

        print(f"mark current char")
        board[x][y] = "!"

        print(f"look around")
        for xdir, ydir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            xo = xdir + x
            yo = ydir + y
            print(f"check for edges")
            if 0 <= xo < ROWS and 0 <= yo < COLS and board[xo][yo] in cur_node:
                dfs(xo, yo, cur_node)

        print(f"replace char")
        board[x][y] = letter

        if not cur_node:
            print(f"if word doesn't exist, pop: {cur_node}")
            root.pop(letter)

    ROWS = len(board)
    COLS = len(board[0])

    trie = {}
    print(f"create trie")

    # Create a Trie data structure which letter are placed into a tree and
    # common letters are in same branch.
    for word in words:
        cur = trie
        for letter in word:
            if letter not in cur:
                cur[letter] = {}

            cur = cur[letter]

        # Use stop char and use word as value.
        cur["#"] = word

    result = []

    print(f"loop through")
    for r in range(ROWS):
        for c in range(COLS):
            # When starting over the search make sure the current letter in
            # start of trie which is the start of a word.
            if board[r][c] in trie:
                dfs(r, c, trie)

    print(f"result: {result}")
    return result


def test_one():
    """pytest word_search_2.py"""
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert set(word_search_2(board, words)) == set(["eat", "oath"])


def test_two():
    """pytest word_search_2.py"""
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    assert word_search_2(board, words) == []

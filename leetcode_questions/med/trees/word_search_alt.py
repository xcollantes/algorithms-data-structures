"""79. Word Search

Given an m x n grid of characters board and a string word, return true if word
exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.
"""


class WordSearch:
    def __init__(self, board: list[list[str]]) -> None:
        self.board = board
        self.max_rows = len(board)
        self.max_cols = len(board[0])

    def word_search(self, word) -> bool:
        """Return if word exists."""
        for row in range(self.max_rows):
            for col in range(self.max_cols):
                if self.__search(row, col, word):
                    return True

        # No matches after iterating over the whole board
        return False

    def __search(self, row: int, col: int, word: str) -> bool:
        """Recursively find word."""
        print("SEARCH for ", word)
        print(f"letter: {self.board[row][col]} r {row} c {col}")

        # Base case where word has been found
        if len(word) == 0:
            return True

        if self.board[row][col] != word[0]:
            return False

        # Check for boundaries Return False if outside the limits of the board.
        # if (
        #     row < 0
        #     or row == self.max_rows
        #     or col < 0
        #     or col == self.max_cols
        #     # Check the first letter which gets "shaved" off for every call of
        #     # `__search()` This case is incase you find a letter you're not
        #     # currently looking for.
        #     or self.board[row][col] != word[0]
        # ):
        # return False

        self.board[row][col] = "#"

        for ro, co in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            rd = ro + row
            cd = co + col
            if 0 <= rd < self.max_rows and 0 <= cd < self.max_cols:
                if self.__search(rd, cd, word[1:]):
                    return True

        self.board[row][col] = word[0]

        return False


def test_word_search():
    """pytest word_search.py."""
    w = WordSearch(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
    )

    assert w.word_search(
        word="ABCCED",
    )

    x = WordSearch(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
    )
    assert x.word_search(
        word="SEE",
    )

    y = WordSearch(
        board=[
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ],
    )
    assert not y.word_search(
        word="ABCB",
    )
    z = WordSearch(
        board=[
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
            ]
        ],
    )

    assert not z.word_search(
        word="AAAAAAAAAAAAAAB",
    )


from leetcode_questions.utils.models.leetcode_data_models import (
    Difficulty,
    Metadata,
    Tags,
)

__metadata__ = Metadata(
    tags=[Tags.ARRAY, Tags.BACKTRACKING, Tags.MATRIX],
    difficulty=Difficulty.MEDIUM,
)

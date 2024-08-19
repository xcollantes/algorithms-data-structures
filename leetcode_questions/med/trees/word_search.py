"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

import logging


class WordSearch:
    def __init__(self, board) -> None:
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
        logging.info("SEARCH: %s", word)
        logging.info(self.board)

        # Base case where word has been found
        if len(word) <= 0:
            return True

        # Check for boundaries
        # Return False if outside the limits of the board
        if (
            row < 0
            or row == self.max_rows
            or col < 0
            or col == self.max_cols
            # Check the first letter which gets "shaved" off for every call of `__search()`
            # This case is incase you find a letter you're not currently looking
            # for.
            or self.board[row][col] != word[0]
        ):
            return False

        revert = False
        self.board[row][col] = "#"

        # Look at each neighbor: up, down, left, right
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # Add offsets and move to next letter
            revert = self.__search(row + row_offset, col + col_offset, word[1:])

            # Case where no matches found
            if revert:
                break

        self.board[row][col] = word[0]

        return revert

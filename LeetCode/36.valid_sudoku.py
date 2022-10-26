"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according
to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
import collections  # Not needed on LeetCode
from typing import List  # Not needed on LeetCode


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or
                        board[row][col] in cols[col] or
                        board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True

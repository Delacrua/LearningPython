"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        visited = set()
        cols = rows = n
        row, col = 0, 0
        d_row, d_col = 0, 1
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(1, cols * rows + 1):
            visited.add((row, col))
            matrix[row][col] = i

            if not (0 <= (row + d_row) < rows
                    and 0 <= (col + d_col) < cols
                    and (row + d_row, col + d_col) not in visited):
                d_row, d_col = d_col, -d_row

            row += d_row
            col += d_col

        return matrix

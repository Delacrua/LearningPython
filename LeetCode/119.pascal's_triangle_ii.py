"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)
        up = rowIndex
        down = 1
        for i in range(1, rowIndex):
            result[i] = int(result[i - 1] * up / down)
            up = up - 1
            down = down + 1
        return result

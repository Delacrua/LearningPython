"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
"""
from typing import List  # Not needed on LeetCode


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * i for i in range(1, numRows + 1)]

        for i in range(1, numRows):
            for j in range(1, i):
                result[i][j] = result[i - 1][j] + result[i - 1][j - 1]

        return result

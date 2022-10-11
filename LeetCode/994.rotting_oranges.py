"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
return -1
"""
from collections import deque  # Not needed on LeetCode


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh, rotten = set(), deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.append((row, col))

        result = 0
        while fresh and rotten:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for coord in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if coord in fresh:
                        fresh.remove(coord)
                        rotten.append(coord)
            result += 1

        return -1 if fresh else result

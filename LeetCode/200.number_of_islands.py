"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def _dfs(grid, row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != "1":
                return
            grid[row][col] = "2"
            _dfs(grid, row - 1, col)
            _dfs(grid, row, col - 1)
            _dfs(grid, row + 1, col)
            _dfs(grid, row, col + 1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    _dfs(grid, row, col)

        return count

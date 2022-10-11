"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly
north, south, east, and west if the neighboring cell's height is less than or equal to the
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""


class Solution(object):
    MOVES = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        atlantic_visited = set()
        pacific_visited = set()

        rows, cols = len(heights), len(heights[0])

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in self.MOVES:
                x, y = i + di, j + dj
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and heights[i][j] <= heights[x][y]:
                    dfs(x, y, visited)

        for i in range(rows):
            dfs(i, 0, pacific_visited)
            dfs(i, cols - 1, atlantic_visited)

        for j in range(cols):
            dfs(0, j, pacific_visited)
            dfs(rows - 1, j, atlantic_visited)

        return list(atlantic_visited & pacific_visited)

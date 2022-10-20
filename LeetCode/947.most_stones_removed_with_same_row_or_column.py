"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
return the largest possible number of stones that can be removed.
"""
from collections import defaultdict  # Not needed on LeetCode


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        visited = set()

        for stone in stones:
            row = stone[0]
            col = stone[1]
            graph[('row', row)].append(stone)
            graph[('col', col)].append(stone)

        def _dfs(stone):
            row, col = stone[0], stone[1]
            visited.add(tuple(stone))

            for stone in graph[('row', row)]:
                if tuple(stone) not in visited:
                    _dfs(stone)
            for stone in graph[('col', col)]:
                if tuple(stone) not in visited:
                    _dfs(stone)

        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                _dfs(stone)
                count += 1

        return len(stones) - count

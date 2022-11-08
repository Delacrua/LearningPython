"""
Given an array of intervals intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                count += 1
                intervals[i + 1][1] = min(intervals[i + 1][1], intervals[i][1])

        return count

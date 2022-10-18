"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])
        comp_interval = intervals[0]

        for interval in intervals[1:]:
            if interval[1] < comp_interval[0]:
                result.append(interval)
            elif interval[0] > comp_interval[1]:
                result.append(comp_interval)
                comp_interval = interval
            else:
                comp_interval[0] = min(comp_interval[0], interval[0])
                comp_interval[1] = max(comp_interval[1], interval[1])
        result.append(comp_interval)

        return result

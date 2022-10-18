"""
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution(object):
    def insert(self, intervals, new_interval):
        """
        :type intervals: List[List[int]]
        :type new_interval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for interval in intervals:
            if interval[1] < new_interval[0]:
                result.append(interval)
            elif interval[0] > new_interval[1]:
                result.append(new_interval)
                new_interval = interval
            else:
                new_interval[0] = min(new_interval[0], interval[0])
                new_interval[1] = max(new_interval[1], interval[1])
        result.append(new_interval)

        return result

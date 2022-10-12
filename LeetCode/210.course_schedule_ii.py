"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi
first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers,
return any of them. If it is impossible to finish all courses, return an empty array.
"""
from collections import defaultdict  # Not needed on LeetCode


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def _DFS(course):
            if visited[course] == -1:
                return False
            if visited[course] == 1:
                return True
            visited[course] = -1  # mark as visited
            for x in graph[course]:
                if not _DFS(x):
                    return False
            visited[course] = 1  # mark as finished
            result.append(course)  # add to result as all dependencies fulfilled
            return True

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        result = []
        visited = [0 for x in range(numCourses)]

        for x in range(numCourses):
            if not _DFS(x):
                return []
        return result


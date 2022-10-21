"""
Given an array of distinct integers candidates and a target integer target, return
a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up
to target is less than 150 combinations for the given input.
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(current[:])
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])

            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result

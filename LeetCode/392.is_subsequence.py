"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str a searched subsequence
        :type t: str a string for findind subsequence
        :rtype: bool
        """
        index_s, index_t = 0, 0
        while index_t < len(t) and index_s < len(s):
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_t += 1
        if index_s == len(s):
            return True
        return False

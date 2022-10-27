"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
import collections  # Not needed on LeetCode


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = collections.Counter(s)
        t_freq = collections.Counter(t)

        return s_freq == t_freq

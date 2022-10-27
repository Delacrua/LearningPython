"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
import collections  # Not needed on LeetCode


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_counter = collections.Counter(s)
        for letter in s:
            if freq_counter[letter] == 1:
                return s.index(letter)
        return -1

from collections import Counter  # not needed in LeetCode
"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []

        left, right = 0, len(p)
        p_freq = Counter(p)
        window_freq = Counter(s[left:right])
        result = [0] if window_freq == p_freq else []

        while right < len(s):
            if s[right] in p_freq:
                window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            if s[left] in window_freq:
                window_freq[s[left]] -= 1
                if window_freq[s[left]] == 0:
                    window_freq.pop(s[left])
            left += 1
            right += 1
            if window_freq == p_freq:
                result.append(left)

        return result


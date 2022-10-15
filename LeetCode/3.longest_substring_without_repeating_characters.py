"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        output = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            else:
                output = max(output, right - left + 1)
            seen[s[right]] = right
        return output

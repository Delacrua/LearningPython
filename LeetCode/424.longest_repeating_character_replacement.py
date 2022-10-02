from collections import deque  # not needed in LeetCode
"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window, char_dict = deque(), {}
        max_len, max_freq = 0, 0

        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
            window.append(char)
            max_freq = max(max_freq, char_dict[char])

            if len(window) <= max_freq + k:
                max_len = max(max_len, len(window))
            else:
                first = window.popleft()
                char_dict[first] -= 1

        return max_len

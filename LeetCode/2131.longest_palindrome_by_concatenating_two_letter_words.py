"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order.
Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
"""
from collections import Counter  # not needed in LeetCode


class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        freq = Counter(words)
        length = 0
        flag = True
        print(freq)
        for item in freq:
            if item == item[::-1]:
                if freq[item] % 2 == 0:
                    length += freq[item]
                else:
                    length += freq[item] - 1
                    if flag:
                        length += 1
                        flag = False
            else:
                if item[::-1] in freq:
                    length += min(freq[item], freq[item[::-1]])

        return length * 2

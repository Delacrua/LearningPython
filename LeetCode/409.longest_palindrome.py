"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome
that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_dict = {}
        for letter in s:
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
        result = sum(value if value % 2 == 0 else value -1 for value in freq_dict.values())

        return result + 1 if any(map(lambda x: x % 2 == 1, freq_dict.values())) else result

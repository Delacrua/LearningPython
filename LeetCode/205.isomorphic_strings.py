"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str a string of ASCII characters
        :type t: str a string of ASCII characters
        :rtype: bool
        """
        set_s, set_t = set(s), set(t)
        set_comb = set(zip(s, t))
        return len(set_s) == len(set_t) == len(set_comb)

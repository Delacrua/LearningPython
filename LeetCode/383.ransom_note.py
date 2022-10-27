"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
import collections  # Not needed on LeetCode


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_freq = collections.Counter(ransomNote)
        mag_freq = collections.Counter(magazine)

        for letter in note_freq:
            if note_freq[letter] > mag_freq[letter]:
                return False
        return True

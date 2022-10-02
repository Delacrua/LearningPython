from collections import Counter  # not needed in LeetCode
"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their
lexicographical order.
"""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        return [word for word, count in sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))[:k]]


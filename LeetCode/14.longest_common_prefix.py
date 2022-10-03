"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = 0
        for item in [set(letters) for letters in zip(*strs)]:
            if len(item) == 1:
                count += 1
            else:
                break
        return strs[0][:count]

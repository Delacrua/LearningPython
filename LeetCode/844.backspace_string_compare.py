"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def process(string):
            result = []
            for c in string:
                if c != '#':
                    result.append(c)
                elif result:
                    result.pop()
            return "".join(result)

        return process(s) == process(t)


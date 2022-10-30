"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '{', '['}
        closing = {')': '(', '}': '{', ']': '['}
        for item in s:
            if item in opening:
                stack.append(item)
            else:
                if not stack:
                    return False
                elif stack[-1] != closing[item]:
                    return False
                else:
                    stack.pop()
        return not stack

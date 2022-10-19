"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in
the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical
expressions, such as eval().
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        stack, number, operand = [], 0, "+"

        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if operand == "-":
                    stack.append(-number)
                elif operand == "+":
                    stack.append(number)
                elif operand == "*":
                    stack.append(stack.pop() * number)
                else:
                    tmp = stack.pop()
                    if tmp // number < 0 and tmp % number != 0:
                        stack.append(tmp // number + 1)
                    else:
                        stack.append(tmp // number)
                operand = s[i]
                number = 0
        return sum(stack)

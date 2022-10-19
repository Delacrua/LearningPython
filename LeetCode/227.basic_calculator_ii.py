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
        number, operand, stack = 0, '+', []

        for index, item in enumerate(s):
            if item.isnumeric():
                number = number * 10 + int(item)
            if item in '+-*/' or index == len(s) - 1:
                if operand == '+':
                    stack.append(number)
                elif operand == '-':
                    stack.append(-number)
                elif operand == '*':
                    j = stack.pop() * number
                    stack.append(j)
                elif operand == '/':
                    j = int(stack.pop() / number)
                    stack.append(j)
                operand = item
                number = 0
        return sum(stack)

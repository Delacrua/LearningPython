"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict_numbers = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        temp1, temp2 = 0, 0

        for digit in num1:
            if digit in dict_numbers:
                temp1 = temp1 * 10 + ord(digit) - 48
        for digit in num2:
            if digit in dict_numbers:
                temp2 = temp2 * 10 + ord(digit) - 48
        return str(temp1 * temp2)

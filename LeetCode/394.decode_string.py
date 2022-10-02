"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly
k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those
repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, current_number, current_string = [], 0, ''

        for char in s:
            if char == '[':
                stack.append(current_string)
                stack.append(current_number)
                current_string, current_number = '', 0
            elif char == ']':
                num = stack.pop()
                previous_string = stack.pop()
                current_string = previous_string + num * current_string
            elif char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                current_string += char

        return current_string


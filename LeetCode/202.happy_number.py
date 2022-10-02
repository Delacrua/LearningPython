"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does
not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def _get_next(number):
            return sum([int(digit) ** 2 for digit in str(number)])

        slow = n
        fast = _get_next(n)
        while fast != 1 and slow != fast:
            slow = _get_next(slow)
            fast = _get_next(_get_next(fast))

        return fast == 1

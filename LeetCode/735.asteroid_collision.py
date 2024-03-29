"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""


class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        result = []
        for asteroid in asteroids:
            while result and result[-1] > 0 and asteroid < 0:
                if result[-1] + asteroid < 0:
                    result.pop()
                elif result[-1] + asteroid > 0:
                    break
                else:
                    result.pop()
                    break
            else:
                result.append(asteroid)
        return result

from collections import Counter  # not needed in LeetCode
"""
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess,
you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong
position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both
secret and guess may contain duplicate digits.
"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        secret_freq, guess_freq = Counter(secret), Counter(guess)

        for i in secret_freq:
            if i in guess_freq:
                cows += min(secret_freq[i], guess_freq[i])

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        return '{0}A{1}B'.format(bulls, cows - bulls)

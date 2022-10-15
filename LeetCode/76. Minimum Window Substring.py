"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        :param s:
        :param t:
        :return:
        """
        if len(s) < len(t):
            return ''

        t_freq = collections.Counter(t)
        chars = len(t_freq.keys())

        s_counter = collections.Counter()
        matches = 0

        result = ''

        left, right = 0, -1

        while left < len(s):
            if matches < chars:
                if right == len(s) - 1:
                    return result
                right += 1
                s_counter[s[right]] += 1
                if 0 < t_freq[s[right]] == s_counter[s[right]]:
                    matches += 1
            else:
                s_counter[s[left]] -= 1
                if t_freq[s[left]] > 0 and s_counter[s[left]] == t_freq[s[left]] - 1:
                    matches -= 1
                left += 1

            if matches == chars:
                if not result:
                    result = s[left:right + 1]
                else:
                    result = min(result, s[left:right + 1], key=len)

        return result


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))

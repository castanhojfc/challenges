"""
Problem:
Find the longest substring without repeating characters.

Solution:
Go through each character.
Store the character indexes in a dictionary.
When a character is found. Keep track of the last streak.
The current streak is given by the current index minus the last streak.
Keep computing the max between the last streak when a character was
found and the current.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstringNaive(self, s: str) -> int:
        result = 0

        if len(s) == 1:
            return 1

        for i, cc in enumerate(s):
            current = {}
            current[cc] = i

            for j, c in enumerate(s[i + 1:]):
                if c in current:
                    result = max(result, len(current))
                    break

                if c not in current:
                    current[c] = j

                result = max(result, len(current))

        return result

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        d = {}
        prev = 0  # size of the previous streak

        for i, c in enumerate(s):
            if c in d and d[c] >= prev:
                prev = d[c] + 1

            d[c] = i
            current_streak = (i + 1) - prev
            res = max(current_streak, res)

        return res


if __name__ == '__main__':
    solution = Solution()

    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))

    s = " "
    print(solution.lengthOfLongestSubstring(s))

    s = "pw"
    print(solution.lengthOfLongestSubstring(s))

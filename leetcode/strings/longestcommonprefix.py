"""
Problem:
Find the longest common prefix in a group of strings.

Solution:
The trick is to find the lexicographically first and last strings.
Then just compare each character, once a diference is found then the result
is given by the index.

Runtimes:
Time: 0(n) * 0(m) + 0(n) * 0(m) -> where m is the size of the longest
string to find the first and last strings. Plus O(m) to find the prefix.
Space: O(1)

https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


if __name__ == '__main__':
    solution = Solution()

    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(solution.longestCommonPrefix(strs))

    strs = ["a"]
    print(solution.longestCommonPrefix(strs))

"""
Problem:
Check if one string is anagram from another.

Solution:
Maintain two hash tables with chracter frequencies.
Check if they are the same.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/valid-anagram/
"""

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for c in s:
            hash_s[c] += 1

        for c in t:
            hash_t[c] += 1

        if hash_s == hash_t:
            return True

        return False


if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"

    print(solution.isAnagram(s, t))

    s = "rat"
    t = "car"

    print(solution.isAnagram(s, t))

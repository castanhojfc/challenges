"""
Problem:
Find the index of the first unique character in a string

Solution:
Just maintain an hashmap with frequencies.
The iterate again through each char, and when the counter is 1 just return the
index.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/first-unique-character-in-a-string/
"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = defaultdict(int)

        for c in s:
            hash[c] += 1

        for i, c in enumerate(s):
            if hash[c] == 1:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()

    s = "leetcode"
    print(solution.firstUniqChar(s))

    s = "loveleetcode"
    print(solution.firstUniqChar(s))

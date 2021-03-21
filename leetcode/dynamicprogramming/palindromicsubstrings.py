"""
Problem:
Find all the palindromic substrings in a string.

Solution:
The dynamic programming state should tell us that a substring from
ith to jth is a palindrome or not. We reuse this information to check
if greater substrings are still a palindrome by just checking the extra
characters at ith - 1 and jth + 1 and if they are equal instead of re-checking
all of the characters.

Single characters are always a palindrome, we can take care of those right
from the start. Double character strings can be easily checked too.
After this is done, we just need to check 3 or more chracters substrings.
For each sub length we keep expanding two pointers and persisting results
and re-using results from the dynamic array.

Runtimes:
Time: O(N^2)
Space: O(N^2)

There is a better solution that provides constant extra space.
Worth revising later, but it does not involve dynamic programming.
It involves explanding around possible centers.

https://leetcode.com/problems/palindromic-substrings/
"""

from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)

        if length <= 0:
            return 0

        dp = defaultdict(dict)

        result = 0

        for i in range(0, length):
            dp[i][i] = True
            result += 1

        for i in range(0, length - 1):
            dp[i][i + 1] = (s[i] == s[i + 1])
            result += 1 if dp[i][i + 1] is True else 0

        for sub_length in range(3, length + 1):
            i = 0
            for j in range(i + sub_length - 1, length):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                result += 1 if dp[i][j] is True else 0
                i += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    print(solution.countSubstrings('abc'))

    print(solution.countSubstrings('aaa'))

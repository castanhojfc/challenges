"""
Problem:
Find the missing number in an array composed by unique numbers.

Solution:
Use a set, populate it with the numbers.
Go through each element of the range if it is not in the set, then return it.

There are more interesting solutions to this problem, worth revisiting later.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/missing-number/
"""

from typing import List


class Solution:
    def missingNumberAlternative(self, nums: List[int]) -> int:
        aux = set(nums)

        for n in range(len(nums) + 1):
            if n not in aux:
                return n

    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        s = 0

        for nb in range(0, len(nums) + 1):
            n += nb

        for nb in nums:
            s += nb

        return n - s


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 0, 1]
    print(solution.missingNumber(nums))

    nnums = [0, 1]
    print(solution.missingNumber(nums))

    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(solution.missingNumber(nums))

    nums = [0]
    print(solution.missingNumber(nums))
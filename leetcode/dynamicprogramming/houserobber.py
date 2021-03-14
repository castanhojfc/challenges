"""
Problem:
Determine the maximum money that can be robbed using an array that
shows the money that they have. Adjacent houses can't be robbed,
otherwise the police is alerted.

Solution:
Pre-compute the first to values.
The maximum number for the next house is given between the max of
the current maximum for the house we are inspecting and the maximum
of the house adjancent to it plus the current number.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/house-robber/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = {0: 0, 1: nums[0]}

        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[len(nums)]


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3, 1]
    print(solution.rob(nums))

    nums = [2, 7, 9, 3, 1]
    print(solution.rob(nums))
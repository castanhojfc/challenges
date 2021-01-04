"""
Challenge:
Find the highest num of the max subarray in an unordered array with positive
and negative numbers.

Solution:
We assume that the value of first element is already the max subarray sum.
Then we go through each element adjacent to it.
Per each iteration we keep updating the current sum.
If the current sum is below 0 we should reset the current sum to the current
value. Otherwise we should keep adding numbers.
Per each iteration we update the result by calculating the max between the
highest value ever found and the current sum.

Runtimes:
Space: O(1)
Time: O(N)

https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        result = current_sum = nums[0]

        for n in nums[1:]:
            current_sum = n if current_sum < 0 else current_sum + n
            result = max(current_sum, result)

        return result


if __name__ == "__main__":
    solution = Solution()

    nums = [1]
    print(solution.maxSubArray(nums))
    nums = [0]
    print(solution.maxSubArray(nums))
    nums = [-2147483647]
    print(solution.maxSubArray(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
    nums = [-2, 1]
    print(solution.maxSubArray(nums))
    nums = [1, 2]
    print(solution.maxSubArray(nums))
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))

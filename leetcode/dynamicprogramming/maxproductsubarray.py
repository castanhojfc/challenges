"""
Problem:
Find the maximum product subarray.

Solution:
Keep track of max and min.
Traverse each number.
The final result will be given between the current result and the new max.
Store the previous max in a temporary variable.
The new max can either be the product between:
the current max and the number, the current min and the number or the number.
The last two checks are used to handle negative numbers and 0.
The new min can either be the product between:
the previous max and the number, the current min and the number or the number.

Runtimes:
Time: O(N)
Space: O(1)

https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 0:
            return 0

        result = _max = _min = nums[0]

        for number in nums[1:]:
            prev_max = _max
            _max = max(_max * number, _min * number, number)
            _min = min(prev_max * number, _min * number, number)
            result = max(result, _max)

        return result


if __name__ == '__main__':
    solution = Solution()

    nums = [2, 3, -2, 4]
    print(solution.maxProduct(nums))

    nums = [-2, 0, -1]
    print(solution.maxProduct(nums))

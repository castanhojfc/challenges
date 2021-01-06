"""
Problem:
Given a target find the position of two elements in the array their sum
is equal to the target.

Solution:
We now that x + y = target. This equation can be x = target - y.
We store the index for each element of the array in a dictionary.
Then we compute the difference between the current number and the target.
If this difference is present in the dictionary, we have found the pair.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSumInefficient(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index, number in enumerate(nums):
            if target - number in d:
                return [index, d[target - number]]
            d[number] = index


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))

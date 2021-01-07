"""
Problem:
Find all possible a + b + c in an array where the sum is equal to 0.
Return all the possible combinations.

Solution:
First sort the array.
Iterate through each a and b.
Because the array is sorted finding in c can be done in log(n) time
using the binary search algorithm.

If after sorting the first element is greater than 0, then we know its
impossible to find a compination. There are no negative numbers.
If a number is positive and the one before is actually the same,
we can skip it, we would repeating the work done in the current iteration.
For the adjacent element to the current element being checked it should be
checked even if it is the same, we can have repeated numbers.
For the remaining numbers we skip the iterations whenever we find a repeated
number.

Runtimes:
Time: O(n*log(n)) + O(n^2*log(n))
Space: depends on the number of solutions

https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return result

        nums.sort()

        for i in range(0, len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                else:
                    c = -nums[i] - nums[j]
                    if self.binary_search(nums, c, j + 1, len(nums) - 1):
                        result.append([nums[i], nums[j], c])

        return result

    def binary_search(self, nums: List[int], target, low, high):
        while low <= high:
            middle = high - (high - low) // 2

            if nums[middle] == target:
                return True
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    nums = []
    print(solution.threeSum(nums))

    nums = [1, 2]
    print(solution.threeSum(nums))

    nums = [1, 2, 1]
    print(solution.threeSum(nums))

    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))

    nums = [0, 0, 0, 0]
    print(solution.threeSum(nums))

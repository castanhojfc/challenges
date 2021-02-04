"""
Problem:
Find the next greater permutation

Solution:
There is a trick:
First find the first decreasing number index.
If not found just reverse the whole list.
If found, reverse all the numbers from the current index to the end.
Then binary search for the new position of the number found initialy
in the current position.
Swap this number with the first decreasing number index.

Runtimes:
Time: O(N + log(N))
Space: O(1)

https://leetcode.com/problems/next-permutation/
"""
import bisect
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                # this means the numbers are in reverse order
                self.reverse(nums, i, len(nums) - 1)
            if nums[i] > nums[i - 1]:
                self.reverse(nums, i, len(nums) - 1)
                j = bisect.bisect(nums, nums[i - 1], i)
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break

    def reverse(self, nums, p, q):
        l, r = p, q
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 2, 3]
    print(nums)

    nums = [3, 2, 1]
    print(nums)

    nums = [1, 1, 5]
    print(nums)

    nums = [1]
    print(nums)
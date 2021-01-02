"""
Problem:
Search the insert index in a sorted array.
The elements are distinct but the target can be an already existent number.
If the number is already existent we want the insertion to happen in the start.
In other words, return the index if it is already present.

Solution:
Search done in a sorted array should always be via binary search,
the first solution provided does not scale well.

Just perform a binary search if the element is found then return the index.
Otherwise if it never found, remeber that whe splitting the lower part is
always adjusted. If the value is lower than all of the elements. The low
pointer is always be 0, otherwise it will be adjusted.

Runtimes:
Second solution:
Space: O(1)
Time: O(log(n))

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

from typing import List


class Solution:
    def searchInsertNaive(self, nums: List[int], target: int) -> int:
        if nums[0] >= target:
            return 0

        length = len(nums)
        if nums[length - 1] == target:
            return length - 1

        if nums[length - 1] < target:
            return length

        for index in range(0, length):
            if target > nums[index] and target <= nums[index + 1]:
                return index + 1

    def searchInsert(self, nums: List[int], target: int) -> int:
        low, result = 0, len(nums) - 1

        while low <= result:
            mid = (low + result) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                low = mid + 1
            else:
                result = mid - 1

        return low


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 3, 5, 6]
    target = 7
    print(solution.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 0
    print(solution.searchInsert(nums, target))

    nums = [1]
    target = 0
    print(solution.searchInsert(nums, target))

    nums = [1]
    target = 1
    print(solution.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 5
    print(solution.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(solution.searchInsert(nums, target))

    nums = [1, 3]
    target = 3
    print(solution.searchInsert(nums, target))

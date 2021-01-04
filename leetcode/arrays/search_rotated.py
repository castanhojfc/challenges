"""
Problem:
Search in a rotated array. Return the index of the target. If not found return
-1.

Solution:
First we need to find the pivot, that is, the index were the deflation of
values occurs.
To find the pivot we can use a slightly modified binary search algorithm.
The first element is the key. If the value in the middle is lower than it, we
now that the target is in the second part of the array. If this happens we
update the low pointer, otherwise we update the high pointer.

Once we know the pivot:
We just try our luck check immediatly if it is the target.
Otherwise, and remember that the first element shows us were the cut happened,
we compare the target to it. If it is lower than the target then we know that
it is in the second part of the array.
Now that we know in which part the target is, we just perform a binary search
on the part that interests us.

Runtimes:
Time: O(2 * log(n))
Space: O(1)

https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = None

        while low <= high:
            mid = high - (high - low) // 2

            if nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1

        return mid

    def search_element(self, nums: List[int], target: int, low: int,
                       high: int) -> int:
        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot = self.find_pivot(nums)

        if target == nums[pivot]:
            return pivot
        elif target < nums[0]:
            return self.search_element(nums, target, pivot + 1, len(nums) - 1)
        else:
            return self.search_element(nums, target, 0, pivot)


if __name__ == "__main__":
    solution = Solution()

    nums = [1]
    target = 0
    print(solution.search(nums, target))

    nums = [0]
    target = 0
    print(solution.search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(solution.search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 7
    print(solution.search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(solution.search(nums, target))

    nums = [1, 3]
    target = 3
    print(solution.search(nums, target))

    nums = [1, 3]
    target = 1
    print(solution.search(nums, target))

    nums = [3, 1]
    target = 3
    print(solution.search(nums, target))

    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))

    nums = [1, 3, 5]
    target = 0
    print(solution.search(nums, target))

    nums = [5, 1, 3]
    target = 5
    print(solution.search(nums, target))

    nums = [3, 5, 1]
    target = 1
    print(solution.search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 4
    print(solution.search(nums, target))

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    print(solution.search(nums, target))

"""
Problem:
Given an array of numbers, do k rotations in such a way that the elements at
the end when shifted get added at the beggining of it.

Solution:
Iterate through each element:
We will need to copy the elements from the length of the array minus k.
These will be put in the beginning. Decrease k by 1 for each iteration.
This way we know when to add elements from the end in the start of the array.
When k reaches 0 we no longer copy.
Copy each current element to an auxiliary array, but only do so
while the current index is lower that the length of the array minus the
original value of k.
Keep track of the original value of k, create an extra variable for this.
A validation needs to be done when k is greater than the length.
If this is true then subtract the length from k that way we will know when
to split and when to copy.
When the current index is greater than the original value of k,
we begin to copy the numbers from the auxiliary array.
An extra variable is used to know how many of them were already copied.

Runtimes:
Space: O(1)
Time: O(n)

https://leetcode.com/problems/rotate-array/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        aux = []
        ori = k

        if k > len(nums):
            ori = k - len(nums)

        copied = 0

        for index in range(0, len(nums)):
            if index <= (len(nums) - 1) - ori:
                aux.append(nums[index])

            if k > 0:
                nums[index] = nums[len(nums) - k]

            k -= 1

            if index >= ori:
                nums[index] = aux[copied]
                copied += 1


if __name__ == "__main__":
    solution = Solution()

    nums = [0, 2, 3, 4, 5, 6, 7]
    k = 2
    result = solution.rotate(nums, k)
    print(nums)

    nums = [-1, -100, 3, 99]
    k = 2
    result = solution.rotate(nums, k)
    print(nums)

    nums = [1, 2]
    k = 3
    result = solution.rotate(nums, k)
    print(nums)

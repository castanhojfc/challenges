"""
Problem:
Return the majority element from an array.
The majority element is the one that appears more than
half of the size of the array.

Solution:
First sort the array.
Then find the element that is in the middle or middle + 1 positions if
the array size is even.

There are more solutions for this problem, worth revisiting later.

Runtimes:
Time: O(nlogn)
Space: O(1) if sorted in place, otherwise O(n)

https://leetcode.com/problems/majority-element/
"""

from collections import defaultdict
from typing import List


class Solution:
    def majorityElementHashTable(self, nums: List[int]) -> int:
        t = len(nums) // 2
        h = defaultdict(int)

        for n in nums:
            h[n] += 1

        for i in h:
            if h[i] > t:
                return i

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[len(nums) // 2]


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 3]
    print(solution.majorityElement(nums))

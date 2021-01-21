"""
Problem:
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Solution:
Heapify the array.
The root element will always point to the minimum.
Keep popping until k - 1.
At the Kth position, return the popped value.

Runtimes:
Time: O(n + (n - k)log(n))
Space: O(1)

https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)

        for _ in range(len(nums) - k):
            heappop(nums)

        return heappop(nums)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    solution = Solution()
    print(solution.findKthLargest(nums, k))

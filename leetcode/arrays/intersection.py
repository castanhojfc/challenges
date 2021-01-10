"""
Problem:
Compute the interception of two arrays.

Solution:
Create two sets for each array. Every element will be unique that way.
Searches done in sets are done in O(1) time.
Go through each element of the biggest array.
Filter if the element exists on the second array.

Runtimes:
Time: O(n + m) the time here is spent converting the arrays to sets.
Space: O(n + m)

https://leetcode.com/problems/intersection-of-two-arrays/
"""

from typing import List


class Solution:
    def intercept(self, set1: set, set2: set) -> List[int]:
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) >= len(set2):
            return self.intercept(set1, set2)
        else:
            return self.intercept(set2, set1)

    def intersectionNaive(self, nums1: List[int],
                          nums2: List[int]) -> List[int]:
        result = set()

        for n in nums1:
            if n in nums2:
                result.add(n)

        for n in nums2:
            if n in nums1:
                result.add(n)

        return list(result)


if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(solution.intersection(nums1, nums2))

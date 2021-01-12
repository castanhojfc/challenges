"""
Problem:
Given an array of integers find if there are duplicates.

Soltution:
Create an aux set.
Iterate through each element.
If the element is not found in the set, add it to it.
Otherwise it has duplicates.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


class Solution:
    def containsDuplicateAlternative(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        if len(set_nums) == len(nums):
            return False

        return True

    def containsDuplicate(self, nums: List[int]) -> bool:
        aux = set()

        for n in nums:
            if n in aux:
                return True
            aux.add(n)

        return False


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 1]
    print(solution.containsDuplicate(nums))

    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums))

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(solution.containsDuplicate(nums))

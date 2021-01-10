"""
Problem:
In a array composed by numbers that are repeated once, find the one that is 
not repeated.

Solution:
Use an hash table.
Go through each element and count the number of times it appears.
Perform another loop, if the count is equal to 1 then that's the solution.

The bit manipulation solution is also interesting and there are other two.
Worth revisiting later!

Runtimes:
Time: O(n*1) = O(n) searching on an hash table takes O(1)
Space: O(n)

https://leetcode.com/problems/single-number/
"""

from typing import DefaultDict, List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = DefaultDict(int)

        for n in nums:
            hash_table[n] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

        return None

    def singleNumberBitManipulation(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n

        return res


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 2, 1]
    print(solution.singleNumber(nums))

    nums = [4, 1, 2, 1, 2]
    print(solution.singleNumber(nums))

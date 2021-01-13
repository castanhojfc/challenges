"""
Problem:
Find the length of the longest consecutive sequence.

Solution:
Use a set to store all the numbers.
Keep track of the longest and current sequences detected.
For each number, we will try to compute the current consecutive sequence,
by performing a loop. While the next number exists in the set,
we increase the streak. Once it does not exist,
we compare the current streak with the biggest found until now.

Runtimes:
Time: O(n) because the while loop is only executed at the beginning of
a sequence.
Space: O(n)

https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aux = set(nums)
        longest_sequence = 1
        current_sequence = 1

        for num in aux:
            if num - 1 not in aux:
                current_num = num
                current_sequence = 1

                while current_num + 1 in aux:
                    current_sequence += 1
                    current_num += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence


if __name__ == "__main__":
    solution = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))

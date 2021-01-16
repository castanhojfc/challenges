"""
Problem:
Increment one to the number represented by an array.

Solution:
Traverse the array in reverse.
If the number found is less than 9, increment 1 and stop.
If not set that value to 0 and continue.
If the first number is a 9 we need to add an extra 1 to the array.

Runtimes:
Time: O(n)
Space: O(1)

https://leetcode.com/problems/plus-one/
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            if digits[i] == 9:
                digits[i] = 0

                if i == 0:
                    digits = [1] + digits

        return digits


if __name__ == "__main__":
    solution = Solution()

    nums = [4, 3, 2, 1]
    print(solution.plusOne(nums))

    nums = [1, 2, 3]
    print(solution.plusOne(nums))

    nums = [0]
    print(solution.plusOne(nums))

    nums = [9]
    print(solution.plusOne(nums))

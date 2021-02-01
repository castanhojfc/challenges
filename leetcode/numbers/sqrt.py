"""
Problem:
Calculate the square root of a number.

Solution:
The result is in the interval between 0 and the number.
For each number we square it. If the result is equal to the number.
Then we have found the solution.
Thus, we just need to perform a binary search in this interval
until the value is found.

Runtimes:
Time: O(log(n))
Space: O(1)

https://medium.com/@rachit.slt/leetcode-square-root-sqrt-da878692c1af
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0

        while left <= right:
            mid = (right + left) // 2

            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == '__main__':
    solution = Solution()

    x = 4
    print(solution.mySqrt(x))

    x = 5
    print(solution.mySqrt(x))

    x = 8
    print(solution.mySqrt(x))

"""
Problem:
Reverse a number.

Solution:
Just keep popping digits by calculating the modulus
of the original number by 10.
When a new number is added multiply the reversed number by 10.
Check if the number is negative or positive from the start and
add the sign at the end.
Before popping check for memory limits. In this case we cannot
store 64-bit integers.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    def reverse(self, x: int) -> int:
        n = True if x < 0 else False
        p = abs(x)
        r = 0

        while p != 0:
            if r * 10 > (2 ** 31):
                return 0

            r = r * 10 + p % 10
            p //= 10

        if n:
            return -r

        return r


if __name__ == '__main__':
    solution = Solution()

    x = 123
    print(solution.reverse(x))

    x = -123
    print(solution.reverse(x))

    x = 120
    print(solution.reverse(x))

    x = 0
    print(solution.reverse(x))

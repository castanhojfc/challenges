"""
Problem:
Compute the power of a number.

Solution:
If the remaining power is even square the current number
and reduce the remaining power in half.
If the power is odd we multiply by x and reduce it by 1.
Continue the process until 1 is reached. When this happens multiply by x.
(I didn't quite understand why we came to this solution, I was a bit tired)

Things to know:
When the power is even.
We just need to compute x^(n/2) and multiply it by itself.
If it is odd:
We just need to compute x^((n-1)/2), multiply it by it self and
multiply by x.

If the power is negative the result is given by the power as it
was done with a positive number divided by 1.
2^-3 = 1 / 2^3

Runtimes:
Time: O(log(n))
Space: O(1)

https://leetcode.com/problems/powx-n/
"""


class Solution:
    def myPowRecursive(self, x: float, n: int) -> float:
        if not n:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2:
            return x * self.myPow(x, n - 1)

        return self.myPow(x * x, n // 2)

    def myPow(self, x, n):
        res = 1
        x = 1 / x if n < 0 else (1 if n == 0 else x)
        m = abs(n)

        while m > 1:
            if m % 2:
                # remaining power is odd
                res *= x
                m -= 1
            x *= x
            m /= 2

        return res * x


if __name__ == '__main__':
    solution = Solution()

    x = 2
    n = 6
    print(solution.myPow(x, n))

    x = 2.00000
    n = 10
    print(solution.myPow(x, n))

    x = 2.10000
    n = 3
    print(solution.myPow(x, n))

    x = 2.00000
    n = -2
    print(solution.myPow(x, n))

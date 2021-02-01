"""
Problem:
Check if a number is Happy.

Solution:
Maintain a set where the sum of the squares of all digits of a number
are stored. When a number is happy eventually the sum of the squares is 1.
But when it is not the number itself will repeat.

Runtimes:
We do not know how many loops will be done.

https://leetcode.com/problems/happy-number/
"""


class Solution:
    def sumSquares(self, n: int) -> int:
        res = 0

        while n > 0:
            res += (n % 10) ** 2
            n //= 10

        return res

    def isHappy(self, n: int) -> bool:
        s = self.sumSquares(n)
        seen = set()

        while s != 1:
            if s in seen:
                return False

            seen.add(s)
            s = self.sumSquares(s)

        return True


if __name__ == '__main__':
    solution = Solution()

    print(solution.isHappy(19))

    print(solution.isHappy(2))

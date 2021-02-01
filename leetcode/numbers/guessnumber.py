"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

from random import randint


class Solution:
    def generate(self, n: int):
        self.number = randint(1, n)

    def guess(self, num: int) -> int:
        if self.number < num:
            return -1

        if self.number > num:
            return 1

        if self.number == num:
            return 0

    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        mid = (low + high) / 2
        val = self.guess(mid)

        while val != 0:
            if val == -1:
                high = mid
            if val == 1:
                low = mid

            mid = (low + high) / 2
            val = self.guess(mid)

        return int(mid)


if __name__ == '__main__':
    solution = Solution()

    n = 1

    solution.generate(n)
    print(f"I generated this number {solution.number}")
    print(solution.guessNumber(n))

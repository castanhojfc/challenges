"""
Problem:
Find the super ugly number at position nth.
A super ugly number is one that has as its prime factors a list of k size.

Solution:
The same thing as the super uglu numbers II problem.
The only difference is that the first pre-computed numbers should match the
prime factors list.

Runtimes:
Time: O(n * log(n))
Space: O(n)

https://leetcode.com/problems/super-ugly-number/
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy()  # perform a deep copy
        heapify(nums)

        # If n is 1 we automatically return this value
        p = 1

        for _ in range(n - 1):
            p = heappop(nums)

            for prime_factor in primes:
                heappush(nums, p * prime_factor)

                if p % prime_factor == 0:
                    break

        return p


if __name__ == '__main__':
    solution = Solution()

    n = 12
    primes = [2, 7, 13, 19]

    print(solution.nthSuperUglyNumber(n, primes))

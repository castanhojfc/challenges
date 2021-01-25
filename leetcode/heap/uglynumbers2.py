"""
Problem:
Write a program to find the nth ugly number.
An ugly number is one that is only divisible by one or more of these numbers
also known as prime factors. They are 2, 3 and 5.

Solution:
We will use a min heap and add pre-computed values to it.
At the nth position the root will be our answer.

To compute in advance remember:
1 -> [2,3,5]
2 -> [4,6,10]
and so on. We multipy per each prime factor.
There's a small optimization that can be done:
Numbers only divisable by 2, should be multiplied by all factors.
Numbers only divisable by 3, should be multiplied by 2 and 3.
Numbers only divisable by 5, should be multiplied by 5.
We go through each prime factor in reverse order and when the modulus is 0
we stop generating to prevent cases like 2*3 and 3*2 from being done.

The heap will always have the smallest value in the root, and that's our
answer per each iteration. We then use this number to compute the next ugly
numbers. Until we reach the end of the cycle.

Runtimes:
Time: O(n * log(n))
Space: O(3*n) -> O(n)

https://leetcode.com/problems/ugly-number-ii/
"""


from heapq import heapify, heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        prime_factors = [5, 3, 2]
        nums = [2, 3, 5]
        heapify(nums)

        # If n is 1 we automatically return this value
        p = 1

        for _ in range(n - 1):
            print(nums)
            p = heappop(nums)

            for prime_factor in prime_factors:
                heappush(nums, p * prime_factor)

                if p % prime_factor == 0:
                    break

        return p


if __name__ == '__main__':
    solution = Solution()

    print(solution.nthUglyNumber(10))

"""
Problem:
Determine the number of ways one can climb stairs.
One can climb one or to steps at a time.

Solution:
Using dynamic programming. We pre-compute the first two results.
We know that the number of steps for n is given by the sum
of the number of steps needed for (n - 1) + (n - 2)
We pre-compute all the values needed until we reach n.

Runtimes:
Time: O(n)
Space: O(n)

There are other strategies that can be used to solve this problem using mathematics.
Might be worth checking out!

https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {
            0: 1,
            1: 2,
        }

        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n - 1]


if __name__ == '__main__':
    solution = Solution()

    n = 2
    print(solution.climbStairs(n))

    n = 3
    print(solution.climbStairs(n))
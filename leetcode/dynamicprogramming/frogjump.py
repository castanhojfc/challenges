"""
Problem:
Check if a frog can jump to the last stone while crossing a river.
An array is given with the stone positions.
After reaching a stone in a k position the next jump can be of k,
k - 1 or k + 1.

Solution:
Track the number of possible previous jumps for each position/stone.
The first stone is always at 0 and the first jump is always of 1 unit.
We use this information to perform quick validations and initialize the
dynamic programming array.
Traverse all the stones:
Traverse all the possible previous positions in the dynamic array.
Compute the next possible positions and add them to the dp array.
Only add to the dp array if the next possible position matches an existing
stone.
If the last position of the dynamic array does not contain any previous
jumps, then the frog can't reach the final stone.

Runtimes:
Time: O(N^2)
Space: O(N^2)

There is a better solution with DFS.
Check this link: https://www.codertrain.co/frog-jump

https://leetcode.com/problems/frog-jump/
"""
from typing import List
from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)

        if len(stones_set) == 0:
            return True

        dp = defaultdict(set)
        dp[1] = set([1])

        for stone in stones:
            if stone == 0:
                continue
            for prev_k in dp[stone]:
                for next_k in {prev_k - 1, prev_k, prev_k + 1}:
                    if stone + next_k in stones_set and next_k != 0:
                        dp[stone + next_k].add(next_k)

        return len(dp[stones[-1]]) > 0


if __name__ == '__main__':
    solution = Solution()

    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    print(solution.canCross(stones))

    stones = [0, 1, 2, 3, 4, 8, 9, 11]
    print(solution.canCross(stones))

"""
Problem:
Obtain the set of all candidates from an array where their sum is equal to the target.

Solution:
Keep track of all possible sums from 0 to the target using all the candidates.
The previously computed sums will be used when needed.
For each candidate perform a loop from 1 to the target.
If the candidate is equal to the current sum then add it to the solutions variable.
If it is lower then get the previous sum combinations for the current sum minus the candidate.
Add the candidate to every possible solution obtained.
The solution is given by the target element of the array.
There is at least another way to solve this problem using backtracking or DFS,
Worth revising later.

Runtimes:
Time: O(elements^N)
Space: O(elements^N)

https://leetcode.com/problems/combination-sum/
"""
from collections import defaultdict
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        # keeps track of all possible sums from 1 to target
        possible_sums = defaultdict(list)

        for candidate in candidates:
            for sum_index in range(1, target + 1):
                if candidate == sum_index:
                    possible_sums[sum_index].append([candidate])
                elif candidate < sum_index:
                    for possible_sum in possible_sums[sum_index - candidate]:
                        possible_sums[sum_index].append(possible_sum +
                                                        [candidate])

        return possible_sums[target]


if __name__ == '__main__':
    solution = Solution()

    candidates = [2, 3, 5]
    target = 8
    print(solution.combinationSum(candidates, target))

    candidates = [2]
    target = 1
    print(solution.combinationSum(candidates, target))

    candidates = [1]
    target = 1
    print(solution.combinationSum(candidates, target))

    candidates = [1]
    target = 2
    print(solution.combinationSum(candidates, target))
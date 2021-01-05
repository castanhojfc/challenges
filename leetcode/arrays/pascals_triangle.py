"""
Problem:
Print the pascal's triagle for a given number of rows.

Solution:
For each row perform a loop from 0 to n + 1 where n is the size of the rows.
For each row the edge elements will always be 1.
Each element inside is given by the sum of the previous results, n - 1
in the current position of the second loop and the previous one.

Runtimes:
Time: O(N^2)
Space: O(N^2)

https://medium.com/@rachit.slt/leetcode-pascals-triangle-f823a26032f2
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = [[1]]

        for n in range(1, numRows):
            if n == 1:
                result.append([1, 1])
            else:
                row = []
                for j in range(0, n + 1):
                    if j == 0 or j == n:
                        row.append(1)
                    else:
                        row.append(result[n-1][j-1] + result[n-1][j])

                result.append(row)

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.generate(6))

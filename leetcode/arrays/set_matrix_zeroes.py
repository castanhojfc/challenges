"""
Problem:
Find zeros in a matrix. Set all elements in their rows and columns as zero.

Solution:
Traverse the entire matrix. If a zero is found save the column and row where it was found.
Traverse a second time. If the current row is in the rows with zeros set the element to 0.
Do the same for columns.

Runtimes:
Time: O(2*(m*n))
Space: O(m+n)

https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        for m in range(0, len(matrix)):
            for n in range(0, len(matrix[0])):
                if matrix[m][n] == 0:
                    rows.add(m)
                    columns.add(n)

        for m in range(0, len(matrix)):
            for n in range(0, len(matrix[0])):
                if n in columns or m in rows:
                    matrix[m][n] = 0


if __name__ == "__main__":
    solution = Solution()

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    print(matrix)

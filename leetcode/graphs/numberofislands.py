"""
Problem:
Find the number of islands in a graph.

Solution:
Traverse all the elements in a grid.
When a 1 is found there's a new island.
Call DFS on this element.
Keep searching in all for positions and replace 1s with 0s.
When another 0 is found or the search is out of bounds end the search.

Runtimes:
Time: O(m*n)
Space: O(m*n) (worst case)

https://leetcode.com/problems/number-of-islands/
"""
from typing import List


class Solution:
    def dfs(self, grid: List[List[str]], i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return

        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        result = 0

        for i in range(len(grid)):
            j = 0
            for j in range(j, len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    result += 1

        return result

if __name__ == '__main__':
    solution = Solution()

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    print(solution.numIslands(grid))

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]

    print(solution.numIslands(grid))

    grid = [["1"],["1"]]

    print(solution.numIslands(grid))
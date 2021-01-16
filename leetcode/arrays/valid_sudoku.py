"""
Problem:
Check if the sudoku board is valid.
No repeated numbers in columns, rows and boxes.

Solution:
Maintain a set for each row, column and box.
Iterate through each element of the board.
Check if the number is present already in the set for that specific row,
column or box.
If so, the soduku board is invalid. Otherwise add it to the set.
The trick here is to compute the number of the box which can be obtained via
mathematics.

Runtimes:
Time: O(1)
Space: O(1)

https://leetcode.com/problems/valid-sudoku/
"""

from typing import DefaultDict, List


class Solution:
    def checkRepeated(self, nums: List[str]):
        counters = DefaultDict()

        for value in nums:
            if value not in counters:
                counters[value] = 0

            counters[value] += 1

        for i in range(1, 10):
            if str(i) in counters and counters[str(i)] >= 2:
                return False

        return True

    def isValidSudokuNaive(self, board: List[List[str]]) -> bool:
        columns = []
        for i in range(0, 9):
            currentCheck = self.checkRepeated(board[i])

            if currentCheck is False:
                return False

            column = []
            for j in range(0, 9):
                column.append(board[j][i])

            columns.append(column)

            currentCheck = self.checkRepeated(column)

            if currentCheck is False:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [
                    str(board[i][j]),
                    str(board[i][j + 1]),
                    str(board[i][j + 2]),
                    str(board[i + 1][j]),
                    str(board[i + 1][j + 1]),
                    str(board[i + 1][j + 2]),
                    str(board[i + 2][j]),
                    str(board[i + 2][j + 1]),
                    str(board[i + 2][j + 2]),
                ]

                currentCheck = self.checkRepeated(square)

                if currentCheck is False:
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == '.':
                    continue

                if value in rows[i]:
                    return False
                else:
                    rows[i].add(value)

                if value in columns[j]:
                    return False
                else:
                    columns[j].add(value)

                box = (i // 3) * 3 + (j // 3)

                if value in boxes[box]:
                    return False
                else:
                    boxes[box].add(value)

        return True


if __name__ == "__main__":
    solution = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(solution.isValidSudoku(board))

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(solution.isValidSudoku(board))

    board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]

    print(solution.isValidSudoku(board))

    board = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "9", ".", ".", ".", ".", ".", ".", "1"],
             ["8", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "9", "9", "3", "5", "7", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "4", "."],
             [".", ".", ".", "8", ".", ".", ".", ".", "."],
             [".", "1", ".", ".", ".", ".", "4", ".", "9"],
             [".", ".", ".", "5", ".", "4", ".", ".", "."]]

    print(solution.isValidSudoku(board))

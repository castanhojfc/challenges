"""
Problem:
Given a n x n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.

Solution:
Put all elements of the matrix in a max heap.
Keep poping until the kth element - 1.
At the kth position just return the poped value.

Runtimes:
Time: O((n * m) + ((n - k) * log(n)))
Space: O(n)

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapify(heap)

        for row in matrix:
            for element in row:
                heappush(heap, -1 * element)

        for _ in range(len(heap) - k):
            heappop(heap)

        return -1 * heappop(heap)


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8

    solution = Solution()
    print(solution.kthSmallest(matrix, k))

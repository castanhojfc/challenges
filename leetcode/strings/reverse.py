"""
Problem:
Reverse a string.

Solution:
Just maintain two pointers.
One that points to the current index.
The other that points to the element that is going to be swapped.
Use a temporary variable to achieve this.
The number of iterations to be done is equal to half the size of the string.
For a string where the size is odd, the element in the middle is not swapped.

Runtimes:
Time: O(n/2) -> O(n)
Space: O(1)

https://leetcode.com/problems/reverse-string/
"""


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        size = len(s)

        for i in range(size // 2):
            p = size - (i + 1)
            temp = s[i]
            s[i] = s[p]
            s[p] = temp



if __name__ == '__main__':
    solution = Solution()

    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)

    s = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s)
    print(s)

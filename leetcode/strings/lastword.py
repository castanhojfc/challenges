"""
Problem:
Get the length of the last word in a string.

Solution:
Split the string and return the length of the last element.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/length-of-last-word/
"""

from string import punctuation


class Solution:
    def lengthOfLastWordNaive(self, s: str) -> int:
        symbols = set(punctuation)
        symbols.add(" ")
        result = 0
        firstLetterFound = False

        for i in range(len(s) - 1, -1, -1):
            if not firstLetterFound and s[i] == ' ':
                continue
            else:
                firstLetterFound = True

            if s[i] in symbols:
                break

            result += 1

        return result

    def lengthOfLastWord(self, s: str) -> int:
        words = s.rsplit(None, 1)

        return len(words[-1]) if words else 0


if __name__ == '__main__':
    solution = Solution()

    s = "Hello World"
    print(solution.lengthOfLastWord(s))

    s = " "
    print(solution.lengthOfLastWord(s))

    s = "a "
    print(solution.lengthOfLastWord(s))

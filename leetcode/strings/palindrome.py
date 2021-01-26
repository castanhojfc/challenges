"""
Problem:
Check if a sentence is a palindrome.

Solution:
Clean the original string first, remove all ponctuation and white spaces.
Set two pointers, one at the start and another at the end.
Iterate until the middle is reached.
If a character in a pointer is different than the other then its not a
palindrome.

Runtimes:
Time: O(n)
Space: O(n)

https://leetcode.com/problems/valid-palindrome/
"""
from string import punctuation
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        exceptions = set(punctuation)
        exceptions.add(' ')
        clean = ""

        for c in s:
            if c not in exceptions:
                clean += c

        clean = clean.lower()

        for i in range(len(clean) // 2):
            j = len(clean) - 1 - i

            if clean[i].lower() != clean[j].lower():
                return False

        return True

    def isPalindromeAlternative(self, s: str) -> bool:
        extracted = "".join(re.findall("[a-zA-Z0-9]+", s.lower()))

        return extracted == extracted[::-1]


if __name__ == "__main__":
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))

    s = "race a car"
    print(solution.isPalindrome(s))

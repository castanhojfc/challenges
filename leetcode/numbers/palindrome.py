"""
Problem:
Check if the number is a palindrome.

Solution:
Check half of the number with the other half.
To get the last digit, just compute the modulus of 10 of a number.
To remove the last digit get the whole division by 10.
When the number is lower than 0 or the last digit is 0,
the digit itself needs to be zero.
We are going to use two variables for this.
The variable passed as the parameter will end up with the first half.
We will store the other half in another variable.
To build the other half, keep popping the last digit and perform a whole
division by 10 on the original number. Always multiply the new variable
by 10 otherwise you're just adding numbers.
We stop the loop when the first half is lower or the same as the other.
For odd numbers we do not want to compare the extra digit that remains in
the second half. We should remove it.

Runtimes:
Time: O(log10(n)) (?)
Space: O(1) (?)
Note: I do not understand why these runtimes are obtained.
I need to check this later.

https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindromeNaive(self, x):
        # Time: O(n) Space: O(n)
        return False if x < 0 else x == int(str(x)[::-1])

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        inverted = 0

        while x > inverted:
            inverted = inverted * 10 + x % 10
            x //= 10

        return x == inverted or x == inverted // 10


if __name__ == '__main__':
    solution = Solution()

    x = 121
    print(solution.isPalindrome(x))

    # x = -121
    # print(solution.isPalindrome(x))

    # x = 10
    # print(solution.isPalindrome(x))

    # x = -101
    # print(solution.isPalindrome(x))

    # x = 11
    # print(solution.isPalindrome(x))

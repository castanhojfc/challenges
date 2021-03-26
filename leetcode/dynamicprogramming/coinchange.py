"""
Problem:
I didn't fully understand this problem, I am a bit tired. ;)
Keep track of the mininum number of coins to make the a specific amount
in a array.

MC = minimum number of coints required to get the change for the amount j.
It is based on this equation: MC(amount) = Min([MC(amount-coin(i))]) + 1 where i = 1 to n
and this difference is greater than 0.
I did not understand how this equiation was derived, although I went
through it using an example on paper. I should revisit this.

Solution:
Time: O(coins*amount)
Space: O(amount)

Runtimes:
https://leetcode.com/problems/coin-change/
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            # x = (dp[i - j] for j in coins if i >= j and dp[i - j] >= 0)
            ways = []
            for j in coins:
                if i >= j and dp[i - j] >= 0:
                    ways.append(dp[i - j])

            dp[i] = min(ways, default=-2) + 1

        return dp[amount]


if __name__ == '__main__':
    solution = Solution()

    coins = [1, 2, 5]
    amount = 11
    print(solution.coinChange(coins, amount))

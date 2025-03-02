from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for k in range(len(coins)):
            dp[k][0] = 1
            for x in range(1, amount+1):
                if x-coins[k] < 0:
                    res = 0
                else:
                    res = dp[k][x-coins[k]]
                dp[k][x] = res + dp[k-1][x]
        return dp[len(coins)-1][amount]


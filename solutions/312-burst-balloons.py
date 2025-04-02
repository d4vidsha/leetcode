from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for l in range(n-1, 0, -1):
            for r in range(l, n-1):
                for i in range(l, r+1):
                    dp[l][r] = max(dp[l][r], dp[l][i-1] + nums[l-1] * nums[i] * nums[r+1] + dp[i+1][r])
        return dp[1][n-2]
    # forward l pointer 1 <= l <= n-1
    # [[0, 0,  0,   0,   0, 0], 
    #  [0, 8, 14,  35,  42, 0],
    #  [0, 0, 24, 108, 136, 0], 
    #  [0, 0,  0,  42,  56, 0],
    #  [0, 0,  0,   0,  21, 0],
    #  [0, 0,  0,   0,   0, 0]]
    
    # backward l pointer from n-1 >= l >= 1
    # [[0, 0,  0,   0,   0, 0],
    #  [0, 8, 36, 136, 143, 0],
    #  [0, 0, 24, 108, 136, 0],
    #  [0, 0,  0,  42,  56, 0],
    #  [0, 0,  0,   0,  21, 0],
    #  [0, 0,  0,   0,   0, 0]]


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        def subproblem(i):
            nonlocal dp
            if i == 0 or i == 1:
                return 1 
            if dp[i] == 0:
                dp[i] = subproblem(i - 1) + subproblem(i - 2)
            return dp[i]
        return subproblem(n)

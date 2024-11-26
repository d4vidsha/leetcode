class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i])
            res = max(res, dp[i][0])
        return res

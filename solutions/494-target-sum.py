from typing import List
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(lambda:-1)
        def solve(x, k):
            if dp[(x, k)] != -1:
                return dp[(x, k)]
            if x == 0 and k == -1:
                dp[(x, k)] = 1
                return dp[(x, k)]
            if k == -1:
                dp[(x, k)] = 0
                return dp[(x, k)]
            dp[(x, k)] = solve(x-nums[k], k-1) + solve(x+nums[k], k-1)
            return dp[(x, k)]

        return solve(target, len(nums)-1)


from math import inf
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = inf
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        return res




if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3,4,5,6,1,2]))

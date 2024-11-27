class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            prev = max(nums[i], prev + nums[i])
            res = max(res, prev)
        return res

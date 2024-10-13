class Solution:
    def rob(self, nums: List[int]) -> int:
        def robi(nums):
            # [..., rob1, rob2, n, ...]
            rob1, rob2 = 0, 0
            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        return max(robi(nums[1:]), robi(nums[:-1]), nums[0])

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) / 2
        opts = set()
        opts.add(0)
        for i in range(len(nums)-1, -1, -1):
            for opt in list(opts):
                opts.add(nums[i]+opt)
            if target in opts:
                return True
        return False

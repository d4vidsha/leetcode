class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # edge case where every number is one
        if sum(nums) == len(nums):
            return sum(nums)-1
        
        # end with a 0 so that counts array will be created correctly
        nums = nums + [0]

        # create the counts array so that any two consecutive 0s will
        # create a 0 element in the counts array.
        # for example, nums: [1, 0, 1, 1, 0, 0, 1] -> counts: [1, 2, 0, 1]
        n = len(nums)
        counts = []
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                counts.append(count)
                count = 0

        # do a final sliding window pass
        res = 0
        for i in range(len(counts) - 1):
            res = max(res, counts[i] + counts[i+1])
        return res

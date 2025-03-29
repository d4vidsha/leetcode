class Solution:
            if nums[i] in toFind:
                return ist(i, toFind[nums[i]])
            toFind[target - nums[i]] = i
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toFind = {}
        for i in range(len(nums)):
            if nums[i] in toFind:
                return i, toFind[nums[i]]
            toFind[target - nums[i]] = i


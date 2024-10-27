class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        def backtrack(constructor, i):
            if i == len(nums):
                subsets.append(constructor)
                return
            backtrack(constructor + [nums[i]], i + 1)
            n = 0
            while i + n < len(nums) and nums[i] == nums[i + n]:
                n += 1
            backtrack(constructor + [], i + n)
        backtrack([], 0)
        return subsets

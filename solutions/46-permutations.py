class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        constructor = []

        def dfs(nums):
            if nums == []:
                res.append(constructor.copy())
                return
            for i in range(len(nums)):
                constructor.append(nums[i])
                dfs(nums[:i] + nums[i+1:])
                constructor.pop()
            return

        dfs(nums)
        return res

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, comb, total):
            if total == target:
                res.append(comb)
                return
            if i == len(nums) or total > target:
                return
            dfs(i, comb + [nums[i]], total + nums[i])
            dfs(i + 1, comb, total)
        
        dfs(0, [], 0)
        return res

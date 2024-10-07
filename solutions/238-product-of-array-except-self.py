class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        pref = [0] * n
        suff = [0] * n
        for i in range(n):
            if i - 1 in range(n):
                pref[i] = nums[i] * pref[i - 1]
            else:
                pref[i] = nums[i]
        for i in range(n-1, -1, -1):
            if i + 1 in range(n):
                suff[i] = nums[i] * suff[i + 1]
            else:
                suff[i] = nums[i]
        
        for i in range(n):
            if i - 1 in range(n):
                output[i] *= pref[i - 1] 
            if i + 1 in range(n):
                output[i] *= suff[i + 1]
        return output


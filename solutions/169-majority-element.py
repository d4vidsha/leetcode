from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        hash = defaultdict(int)
        next = nums[0]
        for i in range(n):
            hash[nums[i]] += 1
        for key in hash:
            if hash[key] > n/2:
                return key
            

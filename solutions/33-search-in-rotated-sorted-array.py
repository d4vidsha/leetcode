from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            if nums[m] >= nums[l]:
                if nums[l] > target or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([3,4,5,6,1,2], 1))

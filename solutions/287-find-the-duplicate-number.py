from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        res = 0
        while True:
            res = nums[res]
            slow = nums[slow]
            if res == slow:
                break
        return res

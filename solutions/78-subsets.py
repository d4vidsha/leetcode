
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = set()
        q = collections.deque([(subset, 0)])
        while q:
            sub, i = q.popleft()
            res.add(tuple(sub))
            if i < len(nums):
                new_sub = sub.copy() + [nums[i]]
                q.append((new_sub, i+1))
                q.append((sub, i+1))
        return [list(r) for r in res]

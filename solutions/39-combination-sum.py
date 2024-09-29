class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        queue = collections.deque([([0] * len(nums), 0)])

        while queue:
            count, total = queue.popleft()
            # a result
            if total == target and tuple(count) not in visited:
                result = []
                for i in range(len(count)):
                    for _ in range(count[i]):
                        result.append(nums[i])
                res.append(result)
                visited.add(tuple(count))
            # not yet reached result
            elif total <= target:
                for i in range(len(nums)):
                    new_count = count.copy()
                    new_count[i] += 1
                    queue.append((new_count, total + nums[i]))

        return res


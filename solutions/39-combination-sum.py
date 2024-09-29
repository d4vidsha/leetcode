class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        queue = collections.deque([[0] * len(nums)])

        while queue:
            count = queue.popleft()
            # calculate total
            total = 0
            for i in range(len(count)):
                total += nums[i] * count[i]
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
                    queue.append(new_count)

        return res


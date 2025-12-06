class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort()

        def recursion(remaining, curr):
            nonlocal res
            if remaining > 0:
                for c in candidates:
                    if curr and curr[-1] <= c:
                        recursion(remaining - c, curr + [c])
                        return
                    recursion(remaining - c, curr + [c])


            elif remaining == 0:
                res.append(curr)

        recursion(target, [])

        return res

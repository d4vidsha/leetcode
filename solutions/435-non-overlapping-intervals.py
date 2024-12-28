class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        currMax = intervals[0][1]
        for i in range(1, len(intervals)):
            if currMax > intervals[i][0]:
                res += 1
                currMax = min(intervals[i][1], currMax)
            else:
                currMax = intervals[i][1]
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                # no overlap
                res.append(intervals[i])
            else:
                interval = res.pop()
                res.append([min(interval[0], intervals[i][0]), max(interval[1], intervals[i][1])])
        return res

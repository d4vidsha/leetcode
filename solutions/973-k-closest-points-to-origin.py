
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            dist = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(pq, (dist, point))

        res = []
        while k > 0:
            _, point = heapq.heappop(pq)
            res.append(point)
            k -= 1
        return res

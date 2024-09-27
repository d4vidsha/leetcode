class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            s1 = -heapq.heappop(pq)
            s2 = -heapq.heappop(pq)
            if s1 > s2:
                heapq.heappush(pq, -(s1 - s2))
        if pq:
            return -pq[0]
        else:
            return 0

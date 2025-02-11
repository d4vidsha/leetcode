import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v, t))

        pq = [(0, k)]
        visited = set()
        while pq:
            totalTime, u = heapq.heappop(pq)
            visited.add(u)
            if len(visited) == n:
                return totalTime
            if u not in adjList:
                continue
            for v, time in adjList[u]:
                if v not in visited:
                    heapq.heappush(pq, (totalTime + time, v))
        return -1


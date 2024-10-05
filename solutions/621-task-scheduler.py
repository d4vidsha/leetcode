
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord("A")] += 1
        pq = [-v for v in counts if v > 0]
        heapq.heapify(pq)
        time = 0
        q = collections.deque()
        while pq or q:
            time += 1

            if not pq:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(pq)
                if count != 0:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
        return time

from collections import defaultdict, deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # in adjacency list
        adjList = defaultdict(list)

        rows = len(matrix)
        cols = len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
                        continue
                    if matrix[r][c] < matrix[r+dr][c+dc]:
                        adjList[(r+dr, c+dc)].append((r, c))
        
        # topological sort via kahn's algorithm
        top_sort = []
        indegree = defaultdict(int)
        for node in adjList:
            indegree[node] = len(adjList[node])

        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if indegree[(r, c)] == 0:
                    queue.append((r, c))

        while queue:
            r, c = queue.pop()
            top_sort.append((r, c))
            for dr, dc in directions:
                if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
                    continue
                if matrix[r][c] < matrix[r+dr][c+dc]:
                    indegree[(r+dr, c+dc)] -= 1
                    if indegree[(r+dr, c+dc)] == 0:
                        queue.append((r+dr, c+dc))
        
        # bottom up dynamic programming
        dp = defaultdict(lambda: 1)
        for node in top_sort:
            for prev in adjList[node]:
                dp[node] = max(dp[node], 1 + dp[prev])
        return max(dp.values()) if dp else 1


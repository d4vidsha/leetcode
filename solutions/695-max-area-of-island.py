class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        visited = set()

        def bfs(r, c):
            area = 0
            q = collections.deque([(r, c)])
            visited.add((r, c))
            while q:
                (r, c) = q.popleft()
                area += 1

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr not in range(rows) or nc not in range(cols):
                        continue
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    res = max(res, area)
        return res

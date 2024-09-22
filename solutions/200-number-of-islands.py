from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ensure grid is not 0z0
        if not grid:
            return 0

        num_islands = 0
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
                for dr, dc in directions:
                    next_r, next_c = r + dr, c + dc

                    # ensure next position is within bounds
                    if next_r not in range(num_rows) or next_c not in range(num_cols):
                        continue
                        
                    next = (next_r, next_c)
                    if grid[next_r][next_c] == "1" and next not in visited:
                        q.append(next)
                        visited.add(next)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1
        return num_islands


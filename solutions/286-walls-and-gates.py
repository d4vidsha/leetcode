from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
            
        while q:
            r, c = q.pop()
            dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in dirs:
                if r+dr < 0 or r+dr > rows - 1 or c+dc < 0 or c+dc > cols - 1:
                    continue
                if grid[r+dr][c+dc] != -1 and grid[r][c] + 1 < grid[r+dr][c+dc]:
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    q.append((r+dr, c+dc))


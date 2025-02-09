
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        numFruits = 0
        q = deque([])
        rotten = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    numFruits += 1
                if grid[r][c] == 2:
                    q.append((0, (r, c)))

        if numFruits == 0:
            return 0

        while q:
            minute, (r, c) = q.popleft()
            grid[r][c] = 2
            rotten.add((r, c))
            if len(rotten) == numFruits:
                return minute
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dr, dc in directions:
                if 0 <= r+dr and r+dr < ROWS and 0 <= c+dc and c+dc < COLS and grid[r+dr][c+dc] == 1:
                    q.append((minute + 1, (r+dr, c+dc)))

        return -1

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()

        def bfs(queue):
            region = set()
            while queue:
                r, c = queue.popleft()
                region.add((r, c))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    if r+dr not in range(rows) or c+dc not in range(cols):
                        continue
                    if (r+dr, c+dc) in region:
                        continue
                    if heights[r][c] <= heights[r+dr][c+dc]:
                        queue.append((r+dr, c+dc))
            return region

        top_row = [(0, c) for c in range(cols)]
        left_col = [(r, 0) for r in range(rows)]
        queue = collections.deque(top_row + left_col)
        pacific = bfs(queue)
        bottom_row = [(rows-1, c) for c in range(cols)]
        right_col = [(r, cols-1) for r in range(rows)]
        queue = collections.deque(bottom_row + right_col)
        atlantic = bfs(queue)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def solve(r, c, prevVal):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prevVal:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]

            res = 0
            for dr, dc in directions:
                res = max(res, 1+solve(r + dr, c + dc, matrix[r][c]))
            dp[r][c] = res
            return res
        
        for r in range(rows):
            for c in range(cols):
                solve(r, c, -1)

        return max([max(i) for i in dp])


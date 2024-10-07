class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * (n+1) for _ in range(m+1)]
        def subproblem(r, c):
            # out of bounds don't affect solution
            if r not in range(m):
                return 0
            if c not in range(n):
                return 0
            if memo[r][c] != 0:
                return memo[r][c]
            if r == m - 1 and c == n - 1:
                return 1
            else:
                memo[r][c] = subproblem(r + 1, c) + subproblem(r, c + 1)
                return memo[r][c]
        return subproblem(0, 0)

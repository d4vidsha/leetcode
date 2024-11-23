class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n+1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    continue
                if length <= 2 or dp[i+1][j-1] == True:
                    dp[i][j] = True
                    res += 1
        return res

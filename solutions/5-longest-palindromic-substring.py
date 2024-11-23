class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        resLen = 0
        res = ""
        for length in range(1, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j] and dp[i+1][j-1] == True:
                        dp[i][j] = True
                if dp[i][j] == True and length > resLen:
                    resLen = length
                    res = s[i:j+1]
        return res

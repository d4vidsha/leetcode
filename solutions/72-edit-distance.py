class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for a in range(len(word1)+1):
            for b in range(len(word2)+1):
                if a == 0 or b == 0:
                    dp[a][b] = max(a, b)
                    continue
                cost = 1 if word1[a-1] != word2[b-1] else 0
                dp[a][b] = min(dp[a][b-1]+1, dp[a-1][b]+1, dp[a-1][b-1]+cost)
        return dp[len(word1)][len(word2)]


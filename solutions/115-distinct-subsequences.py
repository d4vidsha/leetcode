class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for j in range(m+1):
            dp[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[n][m]



        # caaat
        # i
        # cat
        # j
        # cat
        # 133

        # xxyxy
        # xy
        # 3

        # c
        # s[i] == t[j] then 1+dp[i][j-1] (right)
        # # s[i] == t[j] then 1+dp[i-1][j] (up)
        #  caaat
        # c11111
        # a01233
        # t00003

        #  xxyxy
        # x12233
        # y00225

        #  _caaat
        # _111111
        # c011111
        # a001233
        # t000003

        # if i < j then dp[i][j] = 0
        # if i >= j then 
        #     if s[i] == t[j] then dp[i][j-1] (left) + dp[i-1][j] (up)
        #     if s[i] != t[j] then dp[i][j-1] (left)


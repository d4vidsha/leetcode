class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # could be solved with two pointers in O(m+n)
        # dp[2][1] = dp[2][1-1] and s3[2+1] == s2[1] or dp[2-1][1] and s3[2+1] == s1[2]
        # a is the ending index of the substring of s1
        # b is the ending index of the substring of s2
        n = len(s1)
        m = len(s2)
        if n+m != len(s3):
            return False
            
        dp = [[True] * (m+1) for _ in range(n+1)]

        dp[0][0] = True
        for a in range(n+1):
            for b in range(m+1):
                if a == 0 and b == 0:
                    continue
                if a == 0:
                    dp[a][b] = dp[a][b-1] and s3[a+b-1] == s2[b-1]
                elif b == 0:
                    dp[a][b] = dp[a-1][b] and s3[a+b-1] == s1[a-1]
                else:
                    dp[a][b] = dp[a][b-1] and s3[a+b-1] == s2[b-1] or dp[a-1][b] and s3[a+b-1] == s1[a-1]
        return dp[n][m]


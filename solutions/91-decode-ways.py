class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0, 1, 0]
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp = [0] + dp[:2]
                continue
            dp[0] += dp[1]
            if i+1 < len(s) and (s[i] == '1' or s[i] == '2' and ord(s[i+1]) >= ord('0') and ord(s[i+1]) <= ord('6')):
                dp[0] += dp[2]
            dp = [0] + dp[:2]
        return dp[1]

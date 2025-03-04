from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        l = r = 0
        seen = defaultdict(int)
        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            best = max(best, r - l + 1)
            r += 1
        return best


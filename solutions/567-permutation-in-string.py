class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1ht = collections.defaultdict(int)
        for s in s1:
            s1ht[s] += 1
        
        matched = 0
        l, r = 0, 0
        curr_s1ht = s1ht.copy()
        while r < len(s2):
            if s2[r] not in curr_s1ht:
                l = l + 1
                r = l
                curr_s1ht = s1ht.copy()
                matched = 0
            else:
                curr_s1ht[s2[r]] -= 1
                if curr_s1ht[s2[r]] == 0:
                    del curr_s1ht[s2[r]]
                matched += 1
                r = r + 1
            if matched == len(s1):
                return True
        return False

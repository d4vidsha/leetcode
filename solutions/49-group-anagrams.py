from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord("a")] += 1
            res[tuple(counts)] += [word]
        return res.values()


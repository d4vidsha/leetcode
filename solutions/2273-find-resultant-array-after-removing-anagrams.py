from typing import List
from collections import defaultdict

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        for i in range(n - 1, 0, -1):
            if self.anagram(words[i - 1], words[i]):
                words.pop(i)
            print(words)
        return words

    def anagram(self, w1, w2):
        w1Counts = self.counts(w1)
        w2Counts = self.counts(w2)
        return w1Counts == w2Counts
    
    def counts(self, w):
        ht = defaultdict(int)
        for l in w:
            ht[l] += 1
        return ht


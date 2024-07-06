from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    	
	k = max(piles)
	ks = range(1, k + 1)

	l = 0
	r = k -	1

	while l <= r:
	    m = l + (r - l) // 2
	    h1 = 0
	    for p in piles:
	        h1 += math.ceil(p / ks[m])
	    if h1 > h:
	        l = m + 1
	    else:
	        r = m - 1
		k = min(k, ks[m])
	return k

if __name__ == "__main__":
    print(Solution.minEatingSpeed(self, [1,4,3,2], 9))

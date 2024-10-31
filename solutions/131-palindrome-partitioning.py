class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def is_palindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(s):
            if len(s) == 0:
                res.append(path.copy())
                return 
            for i in range(len(s)):
                if not is_palindrome(s[:i+1]):
                    continue
                path.append(s[:i+1])
                backtrack(s[i+1:])
                path.pop()
            return
        backtrack(s)
        return res

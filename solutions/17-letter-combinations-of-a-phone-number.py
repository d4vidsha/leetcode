class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        constructor = []
        digitToLetter = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i):
            if i == len(digits):
                res.append("".join(constructor.copy()))
                return
            for l in digitToLetter[digits[i]]:
                constructor.append(l)
                dfs(i+1)
                constructor.pop()
            return
        dfs(0)
        return res

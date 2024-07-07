from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)

        return res

if __name__ == "__main__":
    print(Solutions.generateParenthesis(None, 3))

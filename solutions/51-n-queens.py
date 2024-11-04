class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ["." * n] * n
        cols = set()
        posDiags = set()
        negDiags = set()
        def backtrack(r):
            if r == n:
                res.append(board.copy())
                return
            for c in range(n):
                if c in cols or r + c in posDiags or r - c in negDiags:
                    continue
                # new c value overwrites original c
                board[r] = board[r][:c] + "Q" + board[r][c+1:]
                cols.add(c)
                posDiags.add(r + c)
                negDiags.add(r - c)
                backtrack(r+1)
                board[r] = board[r][:c] + "." + board[r][c+1:]
                cols.remove(c)
                posDiags.remove(r + c)
                negDiags.remove(r - c)
            return
        backtrack(0)
        return res

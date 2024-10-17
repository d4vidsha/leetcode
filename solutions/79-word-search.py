class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r not in range(rows) or
                c not in range(cols) or
                word[i] != board[r][c] or
                (r, c) in visited):
                return False
            visited.add((r, c))
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0) == True:
                    return True
        return False

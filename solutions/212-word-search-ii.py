class TrieNode:
    def __init__(self, val=None):
        self.child = [None] * 26
        self.val = val
        self.end = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        ROWS = len(board)
        COLS = len(board[0])

        # build the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                index = ord(c) - ord("a")
                if curr.child[index] == None:
                    curr.child[index] = TrieNode(c)
                curr = curr.child[index]
            curr.end = True

        # DFS
        visited = set()
        construct = ""
        def dfs(node, r, c):
            nonlocal construct
            print(construct)
            if (r, c) in visited:
                return
            if (nextNode := node.child[ord(board[r][c]) - ord("a")]) == None:
                return
            visited.add((r, c))
            construct = construct + board[r][c]
            if nextNode.end == True:
                res.add(construct)
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in directions:
                if r+dr not in range(ROWS) or c+dc not in range(COLS):
                    continue
                dfs(nextNode, r+dr, c+dc)
            visited.remove((r, c))
            construct = construct[:-1]

        # search through the graph
        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c)

        return list(res)
        

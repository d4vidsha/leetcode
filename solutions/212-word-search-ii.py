class TrieNode:
    def __init__(self, val=None):
        self.child = [None] * 26
        self.val = val
        self.end = False

    def addWord(self, word):
        curr = self
        for c in word:
            index = ord(c) - ord("a")
            if curr.child[index] == None:
                curr.child[index] = TrieNode(c)
            curr = curr.child[index]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        ROWS = len(board)
        COLS = len(board[0])

        # build the Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)

        # DFS
        visited = set()
        def dfs(node, r, c, word):
            if (r, c) in visited:
                return
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (nextNode := node.child[ord(board[r][c]) - ord("a")]) == None:
                return
            visited.add((r, c))
            if nextNode.end == True:
                res.add(word + board[r][c])
            
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in directions:
                dfs(nextNode, r+dr, c+dc, word + board[r][c])
        
            visited.remove((r, c))
        # search through the graph
        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c, "")

        return list(res)
        

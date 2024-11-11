
class TrieNode():
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.child = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        i = 0
        while i < len(word):
            if not (temp := curr.child[ord(word[i]) - ord("a")]):
                temp = TrieNode(word[i])
            curr.child[ord(word[i]) - ord("a")] = temp
            curr = temp
            i += 1
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(word, curr):
            i = 0
            while i < len(word):
                if curr == None:
                    return False
                if word[i] == ".":
                    for child in [c for c in curr.child if c]:
                        if dfs(word[i+1:], child):
                            return True
                    return False
                index = ord(word[i]) - ord("a")
                curr = curr.child[index]
                i += 1
            if curr:
                return curr.end
            return False
        return dfs(word, curr)

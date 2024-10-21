class TrieNode():
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord("a")
            # ensures node exists
            if node.child[idx] == None:
                node.child[idx] = TrieNode()
            # move to next node
            node = node.child[idx]
        node.wordEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        while i < len(word):
            idx = ord(word[i]) - ord("a")
            if node.child[idx] == None:
                return False
            node = node.child[idx]
            i += 1
        return node.wordEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        i = 0
        while i < len(prefix):
            idx = ord(prefix[i]) - ord("a")
            if node.child[idx] == None:
                return False
            node = node.child[idx]
            i += 1
        return True

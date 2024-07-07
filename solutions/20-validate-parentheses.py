from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for l in s:
            if not q:
                q.append(l)
                continue
            if q[-1] == opposite(l):
                q.pop()
            else:
                q.append(l)
        return not q

def opposite(l):
    if l == ')': return '('
    if l == ']': return '['
    if l == '}': return '{'

if __name__ == "__main__":
    print(Solution.isValid(None, "([]"))

import math
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        max_step = math.ceil(math.log2(n)) + 1
        up = [[-1] * max_step for _ in range(n)]
        for i in range(n):
            up[i][0] = parent[i]
        for j in range(1, max_step):
            for i in range(n):
                if up[i][j-1] != -1:
                    up[i][j] = up[up[i][j-1]][j-1]
        self.up = up
        self.step = 15

    def getKthAncestor(self, node: int, k: int) -> int:
        step = self.step
        while k > 0 and node != -1:
            if k >= 1 << step:
                node = self.up[node][step]
                k -= 1 << step
            else:
                step -= 1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

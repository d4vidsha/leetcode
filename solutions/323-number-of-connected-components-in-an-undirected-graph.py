class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        numUnions = 0
        
        def union(n1, n2):
            nonlocal numUnions
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return
            if rank[r1] < rank[r2]:
                r1, r2 = r2, r1
            numUnions += 1
            par[r2] = r1
            rank[r1] += 1
            return

        def find(node):
            while node != par[node]:
                par[node] = par[par[node]]
                node = par[node]
            return node

        for n1, n2 in edges:
            union(n1, n2)
        return n - numUnions

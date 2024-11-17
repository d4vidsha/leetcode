class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        res = 0
        def dfs(node, prev):
            visited.add(node)
            for n in adj[node]:
                if prev == n:
                    continue
                if n in visited:
                    continue
                dfs(n, node)
        def bfs(node):
            q = collections.deque([(node, None)])
            while q:
                node, prev = q.popleft()
                visited.add(node)
                for n in adj[node]:
                    if prev == n:
                        continue
                    if n in visited:
                        continue
                    q.append((n, node))
        for node in range(n):
            if node in visited:
                continue
            res += 1
            # dfs(node, None)
            bfs(node)
        return res

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
            if not q or depth != q[0][1]:
                res.append(node.val)
        return res

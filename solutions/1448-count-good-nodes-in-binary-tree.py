class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        q = collections.deque([(root, root.val)])
        while q:
            node, max_val = q.popleft()
            if node.val >= max_val:
                good += 1
            if node.left:
                q.append((node.left, max(max_val, node.val)))
            if node.right:
                q.append((node.right, max(max_val, node.val)))
        return good

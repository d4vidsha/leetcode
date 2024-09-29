# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        visited = set()
        while stack:

            # keep adding left without processing any nodes yet
            if stack[-1].left and stack[-1].left.val not in visited:
                stack.append(stack[-1].left)
                continue

            # process node
            node = stack.pop()
            visited.add(node.val)
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                stack.append(node.right)


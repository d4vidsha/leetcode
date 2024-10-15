
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if node == None:
                return 0
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            ret = max(node.val, node.val + leftMax, node.val + rightMax)
            res = max(res, ret, node.val + leftMax + rightMax)
            return ret
        dfs(root)
        return res

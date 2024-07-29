# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right

    def isSameTree(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if n1 == None and n2 == None:
            return True
        if n1 and n2 and n1.val == n2.val:
            left = self.isSameTree(n1.left, n2.left)
            right = self.isSameTree(n1.right, n2.right)
            return left and right
        return False
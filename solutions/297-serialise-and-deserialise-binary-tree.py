# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            lst = []
            if not node:
                return ["N"]
            lst += [str(node.val)]
            lst += preorder(node.left)
            lst += preorder(node.right)
            return lst
        return ",".join(preorder(root))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        data = data.split(",")
        print(data)
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


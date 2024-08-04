# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        t1_leafs = []
        t2_leafs = []
        self.dfs(root1, t1_leafs)
        self.dfs(root2,t2_leafs)
        print(t1_leafs, t2_leafs)
        return True if t1_leafs == t2_leafs else False

    def dfs(self,node,arr):
        if node == None:
            return
        elif node.left == None and node.right == None:
            arr.append(node.val)
            return
        else:
            self.dfs(node.left,arr)
            self.dfs(node.right, arr)
    

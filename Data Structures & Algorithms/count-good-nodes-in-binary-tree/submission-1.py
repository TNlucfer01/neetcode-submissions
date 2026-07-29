# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maxsofar):
            if not root:
                return 0 
            res=1 if root.val>=maxsofar else 0 
            maxsofar=max(root.val,maxsofar)
            res+=dfs(root.left,maxsofar)
            res+=dfs(root.right,maxsofar)

            return res
        return dfs(root,root.val)
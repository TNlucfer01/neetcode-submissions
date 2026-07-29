# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def preorder(root,res):
            if root:
                preorder(root.left,res)
                res.append(root.val)

                preorder(root.right,res)
        preorder(root,res)
        return res[k-1]
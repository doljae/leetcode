# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        left, right = None, None
        
        if not root.left and not root.right:
            return root.val
        
        if root and root.left:
            left = self.evaluateTree(root.left)
        if root and root.right:
            right = self.evaluateTree(root.right)
        
        if root.val == 2:
            return left or right
        else:
            return left and right
        
        
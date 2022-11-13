# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        left, right = [], []
        
        if not root.left and not root.right:
            return [str(root.val)]
        
        if root.left:
            left = self.binaryTreePaths(root.left)
        
        if root.right:
            right = self.binaryTreePaths(root.right)
        
        temp = left + right
        result = []
        for path in temp:
            result.append(str(root.val) + "->" + path)
        
        return result
        
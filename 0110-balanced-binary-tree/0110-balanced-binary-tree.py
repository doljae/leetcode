# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root):
            if not self.result:
                return 0
            left,right = 0,0
            if not root.left and not root.right:
                return 1
            if root.left:
                print(1)
                left = dfs(root.left)
            if root.right:
                print(2)
                right = dfs(root.right)
            print(left,right)
            if abs(left-right)>1:
                self.result=False
            
            return max(left,right)+1
        dfs(root)
        return self.result
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        answers=[]
        def inorder(cur):
            global count
            if not cur:
                return
            inorder(cur.left)
            answers.append(cur.val)
            inorder(cur.right)
            
        inorder(root)
        return answers[k-1]
            
        
        
            
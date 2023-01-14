# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = str(root.val)

        if not root.left and not root.right:
            return result

        if root.left:
            result += "(" + self.tree2str(root.left) + ")"
        else:
            result += "()"
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"

        return result

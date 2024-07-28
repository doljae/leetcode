from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False

        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root: Optional[TreeNode]):
        result = []

        if not root.left and not root.right:
            return [root.val]

        if root.left:
            result += self.dfs(root.left)
        if root.right:
            result += self.dfs(root.right)

        return result

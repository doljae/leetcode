# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = -float("inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return -float("inf")

            left = dfs(root.left)
            right = dfs(root.right)

            self.result = max(self.result,
                              root.val,
                              left,
                              right,
                              left + root.val,
                              right + root.val,
                              left + root.val + right)

            return max(root.val,
                       left + root.val,
                       right + root.val)

        dfs(root)

        return int(self.result)

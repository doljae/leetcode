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
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))

            self.result = max(self.result,
                              left + root.val + right)

            return max(left, right) + root.val

        dfs(root)

        return int(self.result)

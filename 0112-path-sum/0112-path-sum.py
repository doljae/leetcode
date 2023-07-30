# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node: TreeNode, cur_sum: int):
            if self.result is True:
                return

            cur_sum += node.val
            if not node.left and not node.right and cur_sum == targetSum:
                self.result = True
                return
            if node.left:
                dfs(node.left, cur_sum)
            if node.right:
                dfs(node.right, cur_sum)

        if not root.left and not root.right and root.val == targetSum:
            return True
        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)

        return self.result

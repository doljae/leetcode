# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        def check(cur1, cur2):
            if not cur1 and not cur2:
                return True
            if cur1 and not cur2 or not cur1 and cur2:
                return False

            if cur1.val != cur2.val:
                return False

            return check(cur1.left, cur2.left) and check(cur1.right, cur2.right)

        def dfs(cur1, cur2):
            if not cur1:
                return False

            if cur1.val == cur2.val and check(cur1, cur2):
                return True

            return dfs(cur1.left, cur2) or dfs(cur1.right, cur2)

        return dfs(root, subRoot)

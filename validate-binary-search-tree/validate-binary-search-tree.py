# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], left_max=-float("inf"), right_min=float("inf")) -> bool:
        if not root:
            return True

        if left_max >= root.val or root.val >= right_min:
            return False

        return self.isValidBST(root.left, left_max, root.val) and self.isValidBST(root.right, root.val, right_min)
# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    answer = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.answer = []
        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            self.answer.append(cur.val)
            if cur.right:
                dfs(cur.right)

        dfs(root)

        return self.answer == sorted(self.answer) and len(set(self.answer)) == len(self.answer)

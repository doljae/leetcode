from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(cur, flag):

            if not cur.left and not cur.right and flag == 0:
                return cur.val

            answer = 0

            if cur.left:
                answer += dfs(cur.left, 0)

            if cur.right:
                answer += dfs(cur.right, 1)

            return answer

        return dfs(root, -1)
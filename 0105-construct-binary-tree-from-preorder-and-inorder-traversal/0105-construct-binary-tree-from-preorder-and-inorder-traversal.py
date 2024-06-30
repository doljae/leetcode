from typing import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(s1, e1, s2, e2):
            if s1 > e1:
                return None
            value = preorder[s1:e1 + 1][0]
            idx = inorder[s2:e2 + 1].index(value) + s2
            left = idx - s2
            head = TreeNode(value)
            head.left = dfs(s1 + 1, s1 + left, s2, idx - 1)
            head.right = dfs(s1 + left + 1, e1, idx + 1, e2)

            return head

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(s1, e1, s2, e2):
            # print(s1, e1, s2, e2)
            if s1 > e1:
                return None
            value = preorder[s1:e1 + 1][0]
            idx = inorder.index(value)
            right = e2 - idx
            left = idx - s2
            # print(left, right)
            # print("start")
            # print(s1 + 1, s1 + left, s2, idx - 1)
            # print(e1)
            # print(value)
            head = TreeNode(value)
            head.left = dfs(s1 + 1, s1 + left, s2, idx - 1)
            # print(e1)
            # print("done")
            # print(s1, e1, s2, e2)
            # print(s1 + left + 1, e1, idx + 1, e2)
            head.right = dfs(s1 + left + 1, e1, idx + 1, e2)

            return head

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
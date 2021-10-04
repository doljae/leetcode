from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a_node, b_node):
            value = (a_node.val if a_node else 0) + (b_node.val if b_node else 0)
            new_node = TreeNode(value)

            a_left = a_node.left if a_node else None
            b_left = b_node.left if b_node else None

            if not (a_left is None and b_left is None):
                new_node.left = dfs(a_left, b_left)

            a_right = a_node.right if a_node else None
            b_right = b_node.right if b_node else None

            if not (a_right is None and b_right is None):
                new_node.right = dfs(a_right, b_right)

            return new_node

        if not root1:
            return root2

        if not root2:
            return root1

        return dfs(root1, root2)
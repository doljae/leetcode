# Definition for a binary tree node.
from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        def dfs(cur_list):
            cur = cur_list[0]
            cur_node = TreeNode(cur)

            new_list = cur_list[1:]
            if new_list:
                target = len(new_list)
                for i in range(len(new_list)):
                    if new_list[i] > cur:
                        target = i
                        break

                left_list = new_list[:target]
                right_list = new_list[target:]

                if left_list:
                    cur_node.left = dfs(left_list)

                if right_list:
                    cur_node.right = dfs(right_list)

            return cur_node

        return dfs(preorder)

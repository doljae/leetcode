# Definition for a binary tree node.

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(1)]

        def dfs(cur_list):
            if len(cur_list) == 1:
                return [TreeNode(cur_list[0])]
            if not cur_list:
                return [None]

            answer = []
            for index, value in enumerate(cur_list):
                left_subtrees = dfs(cur_list[:index])
                right_subtrees = dfs(cur_list[index + 1:])
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        new_root = TreeNode(value)
                        new_root.left = left_subtree
                        new_root.right = right_subtree
                        answer.append(new_root)

            return answer

        return dfs([i for i in range(1, n + 1)])

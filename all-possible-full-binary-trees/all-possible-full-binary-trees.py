from typing import *
from collections import defaultdict
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = defaultdict(list)
        cache[1].append(TreeNode(0))
        if n == 1:
            return cache[1]

        max_cache_length = n - 2

        for index in range(3, max_cache_length + 1, 2):
            for left in range(1, index, 2):
                right = index - 1 - left
                for left_sub_tree in cache[left]:
                    for right_sub_tree in cache[right]:
                        root = TreeNode(0)
                        root.left = left_sub_tree
                        root.right = right_sub_tree
                        cache[index].append(root)

        answer = []
        for left_length in range(1, max_cache_length + 1, 2):
            right_length = max_cache_length - left_length + 1
            for left_sub_tree in cache[left_length]:
                for right_sub_tree in cache[right_length]:
                    root = TreeNode(0)
                    root.left = deepcopy(left_sub_tree)
                    root.right = deepcopy(right_sub_tree)
                    answer.append(root)
        return answer

# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
        p_seq, q_seq = [], []

        def dfs(cur, seq):
            nonlocal p_seq, q_seq
            if not cur:
                return
            seq.append(cur)
            if not p_seq and cur.val == p.val:
                p_seq = seq[::]
            elif not q_seq and cur.val == q.val:
                q_seq = seq[::]

            dfs(cur.left, seq)
            dfs(cur.right, seq)
            seq.pop()

        dfs(root, [])
        q_seq_set = set(q_seq)
        while p_seq:
            cur_node = p_seq.pop()
            if cur_node in q_seq_set:
                return cur_node

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
from typing import *


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # (node, depth)
        q = deque([(root, 0)])
        stack = []

        while q:
            cur = q.popleft()
            cur_node, cur_depth = cur
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))

            if stack and stack[-1][1] != cur_depth:
                for i in range(len(stack) - 1):
                    stack[i][0].next = stack[i + 1][0]
                stack = []
            stack.append(cur)

        if stack:
            for i in range(len(stack) - 1):
                stack[i][0].next = stack[i + 1][0]

        return root

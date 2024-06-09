# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])
        visited = defaultdict(list)
        visited[0].append(root.val)

        while q:
            cur_node, cur_level = q.popleft()
            new_level = cur_level + 1
            if cur_node.left:
                q.append((cur_node.left, new_level))
                visited[new_level].append(cur_node.left.val)
            if cur_node.right:
                q.append((cur_node.right, cur_level + 1))
                visited[new_level].append(cur_node.right.val)

        result = []
        for key in visited:
            result.append(visited[key][-1])

        return result

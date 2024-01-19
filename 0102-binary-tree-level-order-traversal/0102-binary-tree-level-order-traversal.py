from collections import deque, defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        board = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            cur = q.popleft()
            board[cur[1]].append(cur[0].val)
            if cur[0].left:
                q.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                q.append((cur[0].right, cur[1] + 1))
        print(board)
        answer = []
        for key in board:
            answer.append(board[key])

        return answer

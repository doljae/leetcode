from typing import *
from collections import deque, defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        q = deque([(root, level)])
        seq = deque([(root.val, level)])
        while q:
            cur_node, cur_level = q.popleft()
            if cur_node.left:
                seq.append((cur_node.left.val, cur_level + 1))
                q.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                seq.append((cur_node.right.val, cur_level + 1))
                q.append((cur_node.right, cur_level + 1))
        answer = []
        while seq:
            cur_val, cur_level = seq.popleft()
            temp = [cur_val]
            while seq and seq[0][1] == cur_level:
                temp.append(seq.popleft()[0])
            if cur_level % 2 == 0:
                answer.append(temp)
            else:
                answer.append(temp[::-1])
        return answer
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        cur = root
        q = deque([(cur, 0)])
        seq = deque([])
        while q:
            cur, cur_level = q.popleft()
            seq.append((cur, cur_level))
            if cur.left:
                q.append((cur.left, cur_level + 1))
            if cur.right:
                q.append((cur.right, cur_level + 1))

        while seq:
            cur, cur_level = seq.popleft()
            while seq and cur_level == seq[0][1]:
                cur.next = seq[0][0]
                cur, cur_level = seq.popleft()

        return root

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import defaultdict
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        board = defaultdict(int)

        for node in lists:
            if node:
                cur_head = node
                while cur_head:
                    board[cur_head.val] += 1
                    cur_head = cur_head.next

        head, cur_head = None, None
        for key in sorted(board.keys()):
            if not head:
                head = ListNode(val=key)
                board[key] -= 1
                cur_head = head
                while board[key]:
                    cur_head.next = ListNode(val=key)
                    board[key] -= 1
                    cur_head = cur_head.next
            else:
                while board[key]:
                    cur_head.next = ListNode(val=key)
                    board[key] -= 1
                    cur_head = cur_head.next

        return head

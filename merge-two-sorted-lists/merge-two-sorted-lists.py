from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:
            return l2

        if not l2:
            return l1

        h1, h2 = l1, l2

        answer = ListNode(-1)
        cur = answer

        while h1 and h2:
            if h1.val >= h2.val:
                cur.next = ListNode(h2.val)
                h2 = h2.next
            else:
                cur.next = ListNode(h1.val)
                h1 = h1.next
            cur = cur.next
        if h1:
            cur.next = h1
        elif h2:
            cur.next = h2

        return answer.next
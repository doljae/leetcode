from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        trace = []
        cur = head
        while cur:
            trace.append(cur)
            cur = cur.next
        trace.sort(key=lambda x: x.val)

        for i in range(1, len(trace)):
            trace[i - 1].next = trace[i]
            
        trace[-1].next = None
        return trace[0]

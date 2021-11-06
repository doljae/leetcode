from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200)
        dummy.next = head
        cur = dummy

        while cur:
            while cur and cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next

        return dummy.next

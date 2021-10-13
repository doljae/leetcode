from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        temp.next = head
        cur = temp

        while cur:
            flag = False
            while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                cur.next = cur.next.next
                flag = True
            if flag:
                cur.next = cur.next.next
            if not flag:
                cur = cur.next

        return temp.next
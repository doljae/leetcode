# Definition for singly-linked list.
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        n2 = []
        while l2:
            n2.append(l2.val)
            l2 = l2.next

        n3, n4 = 0, 0
        while n1:
            length = len(n1)
            c = n1.pop()
            n3 += (c * pow(10, length - 1))
        while n2:
            length = len(n2)
            c = n2.pop()
            n4 += (c * pow(10, length - 1))

        result = list(str(n3 + n4))

        dummy = ListNode(-1)
        cur = dummy
        while result:
            c = result.pop()
            cur.next = ListNode(int(c))
            cur = cur.next

        return dummy.next
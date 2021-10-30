from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        p1, p2 = head, head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        right = p1.next
        p1.next = None
        left = head
        left_sorted_list = self.sortList(left)
        right_sorted_list = self.sortList(right)

        return self.merge(left_sorted_list, right_sorted_list)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        temp = ListNode(0)
        cur = temp

        while left and right:
            if left.val >= right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next

        cur.next = left if left else right
        return temp.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        if not head:
            return 0

        seq = []
        cur = head
        while cur:
            seq.append(str(cur.val))
            cur = cur.next

        return int("".join(seq), 2)

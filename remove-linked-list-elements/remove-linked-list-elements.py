class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        while head and head.val == val:
            head = head.next

        if not head:
            return None

        cur = head
        while cur and cur.next:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

        return head
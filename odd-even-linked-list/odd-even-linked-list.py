class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        h1, h2 = head, head.next
        s1, s2 = head, head.next
        while True:
            if h1.next and h1.next.next:
                h1.next = h1.next.next
                h1 = h1.next
            if h2.next and h2.next.next:
                h2.next = h2.next.next
                h2 = h2.next
            else:
                h2.next = None
                break
        h1.next = s2
        return head
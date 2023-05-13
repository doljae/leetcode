# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        temp = []
        while head.next:
            temp.append(head.val)
            head = head.next
        temp.append(head.val)
        temp.sort()
        result = ListNode(temp[0])
        cur = result
        for num in temp[1:]:
            cur.next = ListNode(num)
            cur = cur.next

        return result
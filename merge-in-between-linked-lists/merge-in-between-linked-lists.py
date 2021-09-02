# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        merge_head, merge_tail = list1, list1

        cur = list1
        cur_index = 0
        while cur_index != b:
            cur = cur.next
            cur_index += 1

            if cur_index == a - 1:
                merge_head = cur

            if cur_index == b:
                merge_tail = cur.next
                break

        merge_head.next = list2

        temp = list2
        while temp.next:
            temp = temp.next

        temp.next = merge_tail

        return list1
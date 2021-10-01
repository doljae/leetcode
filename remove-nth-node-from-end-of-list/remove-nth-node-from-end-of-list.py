# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        if not cur:
            return None
        
        visited=[TreeNode(-1)]
        visited[0].next=cur
        
        while cur:
            visited.append(cur)
            cur=cur.next
        
        target = len(visited)-n
        
        visited[target-1].next = visited[target+1] if target+1<len(visited) else None
        
        return visited[0].next
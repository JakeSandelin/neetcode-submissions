# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        child, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = child
            child = cur
            cur = tmp
            
        
        return child
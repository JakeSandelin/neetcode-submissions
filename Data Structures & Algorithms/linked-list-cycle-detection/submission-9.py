# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        c1 = c2 = head
        if not c2:
            return False

        while c2.next and c2.next.next:
            if c1.next == c2.next.next:
                return True
            c1 = c1.next
            c2 = c2.next.next
        
        return False
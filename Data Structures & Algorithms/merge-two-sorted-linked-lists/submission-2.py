# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list2.val < list1.val:
            cur = list2
            list2 = list2.next 
        else:
            cur = list1
            list1 = list1.next
        head = cur

        while list1 and list2:
            if list2.val < list1.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            else:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
        

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # do i need a node wrapper? idk man this seems easy no heap needed.
        dummy = ListNode(777)
        current = dummy

        # loop while they are still try
        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                current = current.next
                list2 = list2.next

            elif list2.val > list1.val:
                current.next = list1
                current = current.next
                list1 = list1.next

        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # efficient method involves a heap, and then i need to remember linked lists
        # to start off we need to push the first element of each linked list into the min heap
        # after that we can commence pop, if pop replace with an element of the same list...
        # lets start there.
        
        # init heap
        heap = []

        # add first val and node of the linked list?
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # at this point we have some linked list, still pointed at the node
        # print(heap)

        # we need some way to track everything thats popped
        dummy = ListNode(777)
        head = dummy # i think this line is unncessary
        current = head

        # we need a result array so that we can keep track of all the values that we are popping
        # and we need to pop until our heap is empty
        # empty heap = all lists exhausted
        while heap:
            # unpack all the values in the popped tuple
            val, i, node = heapq.heappop(heap)

            # now set the node next and move to the next node
            current.next = node
            current = current.next # or perhaps just head ?

            # chcek to see if theres something else to add to the list
            if current.next != None:
                heapq.heappush(heap, (current.next.val, i, current.next))


        return dummy.next









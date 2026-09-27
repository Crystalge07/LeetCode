# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # if theres no head aka list is empty
            return None # return None cus empty list
        # walking through the list
        prev = None 
        curr = head
        while curr is not None: # while the current head is still in the list 
            nxt = curr.next # next = the current nodes next
            curr.next = prev # actually doing the reversal, setting the current nodes next to its prev node 
            prev = curr # iterating along 
            curr = nxt # iterating along 
        return prev #by the end, prev should be the head of the new list         

# ok so basically first checks if the head is there, returning nothing if the list is empty
# assigns prev to nothing, and curr to head (beginning of the list)
# iterates through the list while the curr is not nothing
# assigns the nxt node to current's next node, then flips the list by assigning current node's next to current's prev node 
# then assigns current to nxt, and prev to curr (iterating along the list)
# ends by returning prev, which by now is the head of the reversed list
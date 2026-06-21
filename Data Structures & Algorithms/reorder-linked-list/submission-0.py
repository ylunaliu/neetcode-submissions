# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find first and second half
        # take second portion, reverse it
        # Then merge
        slow = head
        fast = head.next
        #slow.next = second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next 
        slow.next = None #splitting, this is first half
        prev= None
        # Need to revserse it 
        while second:
            tmp = second.next
            second.next = prev #reverse the pointer
            prev = second
            second = tmp
        
        # Merge list
        first, second = head, prev
        while second: #second always shorter than first
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2


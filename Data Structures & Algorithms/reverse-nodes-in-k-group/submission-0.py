# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        groupPrev = dummy


        def getKth(curr, k):
            while curr and k>0:
                curr = curr.next
                k-=1
            return curr

        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next
            tmp = groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr=nxt
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next


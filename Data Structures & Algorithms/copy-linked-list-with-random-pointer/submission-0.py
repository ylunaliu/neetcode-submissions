"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Initilize a deep copy
        # Need to do two passes, first pass to create copy for the node
        # Also going to create a hashmap

        oldToCopy = {None:None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur]  = copy
            cur = cur.next

        cur = head
        while cur:
            #Now set the pointer
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
        
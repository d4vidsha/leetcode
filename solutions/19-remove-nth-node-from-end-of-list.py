from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        l = dummy
        r = head
        ri = 1
        while ri <= n:
            r = r.next
            ri += 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next


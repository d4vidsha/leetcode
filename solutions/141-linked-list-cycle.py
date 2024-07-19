from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        assert(head)
        slow = head
        fast = head.next
        while fast and fast.next:
            assert(slow)
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False





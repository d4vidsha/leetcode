# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while fast != None:
            if fast.next == None:
                break
            slow = slow.next
            fast = fast.next.next
        
        # remove slow node
        slow.next = slow.next.next

        return dummy.next

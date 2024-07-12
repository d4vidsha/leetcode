# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        l = res
        while list1 or list2:
            if list1 == None:
                l.next = list2
                break
            elif list2 == None:
                l.next = list1
                break
            if list1.val > list2.val:
                l.next = ListNode(val=list2.val)
                list2 = list2.next
            else:
                l.next = ListNode(val=list1.val)
                list1 = list1.next
            l = l.next
        return res.next

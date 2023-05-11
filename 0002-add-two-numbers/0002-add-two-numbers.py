# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        carry = 0
        while l1 is not None or (l2 is not None):
            if l2 is None:
                l2 = ListNode()
            if l1 is None:
                l1 = ListNode()
            if (l1.val+l2.val+carry)>9:
                    node = ListNode(((l1.val+l2.val+carry)%10))
                    carry = 1
            else:
                node = ListNode((l1.val+l2.val+carry))
                carry = 0
            if curr is None:
                curr = head = node
            else:
                curr.next = node
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head
        
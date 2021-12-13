#https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseToInt(li):
            result = []
            while li:
                result.append(str(li.val))
                li = li.next
            return int(''.join(result[::-1]))

        def toList(val):
            head = None
            v_list = list(str(val))
            for v in v_list:
                cur = ListNode(v)
                head, head.next = cur, head
            return head

        val = reverseToInt(l1) + reverseToInt(l2)
        return toList(val)
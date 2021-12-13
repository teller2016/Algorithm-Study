# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 반복 이용
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None
        while head:
            rev, rev.next, head = head, rev, head.next
        return rev

# 재귀 이용
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(node, rev):
            if not node:
                return rev
            rev, rev.next, node = node, rev, node.next
            return recursive(node, rev)

        return recursive(head, None)
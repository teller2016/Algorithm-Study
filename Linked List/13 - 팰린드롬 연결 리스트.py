# https://leetcode.com/problems/palindrome-linked-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 런너 기법 사용
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deque = collections.deque()

        while head:
            deque.append(head.val)
            head = head.next

        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False

        return True
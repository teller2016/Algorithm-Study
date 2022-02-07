# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 값만 바꾸기
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head

# 노드를 바꾸기기
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        head = ListNode()
        head.next = node
        prev = head

        while node and node.next:
            node_next = node.next
            prev.next, node.next, node_next.next = node_next, node_next.next, node
            prev, node = node, node.next

        return head.next
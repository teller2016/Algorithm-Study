# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)

            index = node[1]
            result.next = node[2]

            result = result.next

            if result.next:
                heapq.heappush(heap, (result.next.val, index, result.next))

        return root.next
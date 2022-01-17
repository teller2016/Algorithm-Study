# https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))

        result = []
        while heap:
            height, num = heapq.heappop(heap)
            result.insert(num, [-height, num])

        return result
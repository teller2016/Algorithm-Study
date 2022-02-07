# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            val = x ** 2 + y ** 2
            heapq.heappush(heap, [val, x, y])

        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result
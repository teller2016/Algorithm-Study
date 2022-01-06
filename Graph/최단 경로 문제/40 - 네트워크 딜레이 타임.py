# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for a, b, cost in times:
            graph[a].append([b, cost])

        dist = collections.defaultdict(int)
        Q = [[0, k]]

        while Q:
            cost, cur = heapq.heappop(Q)
            if cur not in dist:
                dist[cur] = cost
                for next_node, time in graph[cur]:
                    heapq.heappush(Q, [cost + time, next_node])

        if len(dist) != n:
            return -1

        return max(dist.values())
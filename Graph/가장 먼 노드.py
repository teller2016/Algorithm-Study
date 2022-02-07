# https://programmers.co.kr/learn/courses/30/lessons/49189
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다.

import collections
import heapq

def solution(n, edge):
    graph = collections.defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    visited = collections.defaultdict(int)
    Q = [[0, 1]]  # 거리, 노드

    while Q:
        cur_cost, cur = heapq.heappop(Q)
        if cur not in visited:
            visited[cur] = cur_cost
            for next_node in graph[cur]:
                heapq.heappush(Q, (cur_cost + 1, next_node))
    max_cost = max(visited.values())
    return list(visited.values()).count(max_cost)

# n	vertex	return
# 6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

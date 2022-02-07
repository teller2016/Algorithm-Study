# https://programmers.co.kr/learn/courses/30/lessons/43162

import collections
def solution(n, computers):
    graph = collections.defaultdict(list)

    for i in range(len(computers)):
        for j in range( i +1 ,n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    visited = collections.defaultdict(int)

    result = 0

    for x in range(n):
        if x not in visited:
            result += 1
            Q = collections.deque([x])
            while Q:
                cur = Q.popleft()
                if cur not in visited:
                    visited[cur] = True
                    for num in graph[cur]:
                        Q.append(num)
    return result
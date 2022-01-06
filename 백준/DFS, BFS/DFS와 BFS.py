# https://www.acmicpc.net/problem/1260

import collections

n, m, start = map(int, input().strip().split(' '))

graph = collections.defaultdict(list)
for _ in range(m):
    a,b = map(int, input().strip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

dfs = []
stack = [start]
while stack:
    v = stack.pop()
    if v not in dfs:
        dfs.append(v)
        for w in sorted(graph[v], reverse=True):
            stack.append(w)

bfs = [start]
queue = [start]
while queue:
    v = queue.pop(0)
    for w in sorted(graph[v]):
        if w not in bfs:
            bfs.append(w)
            queue.append(w)
print(*dfs)
print(*bfs)
# https://www.acmicpc.net/problem/2606

import collections

n = int(input())
m = int(input())

graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().strip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = collections.defaultdict(bool)
stack = [1]

while stack:
    cur = stack.pop()
    if cur not in visited:
        visited[cur] = True
        for w in graph[cur]:
            stack.append(w)

print(len(visited) - 1)

### dfs 방식
dic2 = {}
def dfs2(cur):
    if cur not in dic2:
        dic2[cur] = 1
        for w in graph[cur]:
            dfs2(w)

dfs2(1)
print(dic2)
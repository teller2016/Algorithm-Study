# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if g[x][y] == 1:
        g[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().strip().split(' '))
    g = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        g[x][y] = 1

    total = 0
    for x in range(n):
        for y in range(m):
            if g[x][y] == 1:
                total += 1
                dfs(x, y)
    print(total)

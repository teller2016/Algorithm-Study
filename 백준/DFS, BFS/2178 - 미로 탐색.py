# https://www.acmicpc.net/problem/2178
import collections

N, M = map(int, input().strip().split(' '))
g = []

for _ in range(N):
    g.append(list(map(str, input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def solution2(g, N, M):
    Q = collections.deque()
    Q.append([0,0])
    g[0][0] = 1
    while Q:
        i,j = Q.popleft()

        for r in range(4):
            nx, ny = i+dx[r], j+dy[r]
            if nx>=0 and nx<N and ny>=0 and ny<M and g[nx][ny] == '1':
                g[nx][ny] = g[i][j] + 1
                Q.append([nx,ny])
    #print(g)
    print(g[N-1][M-1])



solution2(g, N, M)


# graph를 int형으로 받음
def solution(g, N, M):
    Q = collections.deque()
    Q.append([0,0,1])

    while Q:
        i,j,dist = Q.popleft()
        if i==N-1 and j==M-1:
            return dist
        if i>=0 and i<N and j>=0 and j<M and g[i][j] > 0:
            if g[i][j] == 1:
                if i==0 and j==0:
                    g[i][j] = -1
                else:
                    g[i][j] = dist

                for r in range(4):
                    Q.append([i + dx[r], j + dy[r], dist + 1])
            elif g[i][j] < dist:
                continue
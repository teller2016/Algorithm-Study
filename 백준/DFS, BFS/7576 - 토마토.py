# https://www.acmicpc.net/problem/7576
import collections

dx = [1,-1,0,0]
dy = [0,0,1,-1]

M, N = map(int, input().strip().split(' '))
box = []
for _ in range(N):
    box.append(list(map(int, input().strip().split(' '))))

def solution2(box, M, N):
    Q = collections.deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                Q.append([i,j])

    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                Q.append([nx,ny])

    result = -1
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                print(-1)
                return
            result = max(result, box[i][j])
    print(result-1)


# 내풀이
def solution(box, M, N):
    day = 0 # 총 일수
    total = 0 # 총 채워야하는 토마토 개수
    for row in box:
        total += row.count(0)

    Q = collections.deque()

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                Q.append([i,j])

    while Q:
        new_Q = collections.deque()
        day += 1
        while Q:
            x,y = Q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx>=0 and nx<N and ny>=0 and ny<M and box[nx][ny] == 0:
                    box[nx][ny] = 1
                    total -= 1
                    new_Q.append([nx,ny])
        Q = new_Q

    if total == 0:
        print(day-1)
    else:
        print(-1)

solution2(box, M, N)


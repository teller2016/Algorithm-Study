# https://www.acmicpc.net/problem/2667
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input())))

total = 0
count = 0
result = []

def dfs(i,j):
    global count
    if i<0 or i>=N or j<0 or j>=N:
        return

    if M[i][j] == 1:
        count += 1
        M[i][j] = 0
        for m in range(4):
            dfs(i+dx[m], j+dy[m])


for i in range(N):
    for j in range(N):
        if M[i][j] == 1:
            total += 1
            dfs(i,j)
            result.append(count)
            count = 0

print(total)
for v in sorted(result):
    print(v)
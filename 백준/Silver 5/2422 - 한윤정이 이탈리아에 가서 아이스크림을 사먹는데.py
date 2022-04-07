import itertools

N, M = map(int, input().split())
ice = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ice[a][b] = True
    ice[b][a] = True

result =0
for i in itertools.combinations(range(1,N+1), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result += 1

print(result)
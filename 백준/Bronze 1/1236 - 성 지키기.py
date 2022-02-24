N, M = map(int, input().split())
castle = []
for _ in range(N):
    castle.append(input())

row_total = 0
for row in castle:
    if 'X' not in row:
        row_total += 1

col_total = 0
for i in range(len(castle[0])):
    if 'X' not in [castle[j][i] for j in range(len(castle))]:
        col_total += 1

result = max(row_total, col_total)
print(result)
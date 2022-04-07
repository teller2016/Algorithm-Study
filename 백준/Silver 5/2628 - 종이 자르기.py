col, row = list(map(int, input().split()))
n = int(input())

rowCut = [0, row]
colCut = [0, col]
for _ in range(n):
    a, b = list(map(int, input().split()))
    if a == 0:
        rowCut.append(b)
    else:
        colCut.append(b)
rowCut.sort()
colCut.sort()

rowLen = []
colLen = []
for i in range(len(rowCut)-1):
    rowLen.append(rowCut[i+1]-rowCut[i])
for i in range(len(colCut)-1):
    colLen.append(colCut[i+1]-colCut[i])

print(max(rowLen)*max(colLen))
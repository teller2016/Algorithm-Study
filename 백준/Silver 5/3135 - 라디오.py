save = []
A, B = map(int, input().split())

count = abs(B - A)

n = int(input())
for _ in range(n):
    save.append(int(input()))

for s in save:
    count = min(count, abs(B-s)+1)

print(count)
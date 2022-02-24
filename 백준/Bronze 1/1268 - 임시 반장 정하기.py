# https://www.acmicpc.net/problem/1268
import collections

N = int(input())
students = []
for _ in range(N):
    students.append(list(map(int, input().split())))

count = collections.defaultdict(int)

for i in range(len(students) - 1):
    for j in range(i+1, len(students)):
        for a, b in zip(students[i], students[j]):
            if a == b:
                count[i] += 1
                count[j] += 1
                break

sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
if not sorted_count:
    print(1)
else:
    print(sorted_count[0][0] + 1)

import itertools
import collections
N = int(input())

result = collections.defaultdict(int)

for i in range(1,N+1):
    li = list(map(int, input().split()))
    combi = list(itertools.combinations(li, 3))
    for iter in combi:
        if result[i] < (sum(iter)%10):
            result[i] = sum(iter)%10

print(sorted(result.items(), key = lambda x: (-x[1], -x[0]))[0][0])
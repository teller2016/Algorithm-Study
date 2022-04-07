import collections
import math

N = input()
numbers = collections.defaultdict(int)
for n in N:
    numbers[int(n)] += 1

result = math.ceil((numbers[6]+numbers[9])/2)
for num, cnt in numbers.items():
    if num in [6,9]:
        continue
    result = max(result, cnt)

print(result)
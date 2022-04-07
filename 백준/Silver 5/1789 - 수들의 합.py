
n = int(input())
result = 0
i = 0
while True:
    i += 1
    if n - i == 0:
        break
    elif n - i < i+1:
        continue
    n -= i
    result += 1
print(result+1)
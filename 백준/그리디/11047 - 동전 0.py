N, K = map(int, input().split(" "))

coins = list()
for _ in range(N):
    coins.append(int(input()))

result = 0
for coin in coins[::-1]:
    if coin <= K:
        n = K // coin
        K -= n * coin
        result += n

print(result)

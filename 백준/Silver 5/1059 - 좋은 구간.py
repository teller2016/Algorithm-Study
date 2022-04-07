L = int(input())

S = list(map(int, input().split()))
S.append(0)
S.sort()

n = int(input())

result = 0

for i in range(len(S)-1):
    if S[i] == n or S[i+1] == n:
        break
    elif S[i] < n < S[i+1]:
        result = (n - S[i]) * (S[i+1]-n) -1

print(result)

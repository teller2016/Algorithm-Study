# https://www.acmicpc.net/problem/1296
import collections

myTeam = input()
N = int(input())

result = []

for _ in range(N):
    name = input()

    string = myTeam + name
    counter = collections.Counter(string)
    L = counter['L']
    O = counter['O']
    V = counter['V']
    E = counter['E']
    result.append([((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100, name])

print(sorted(result, key=lambda x : (-x[0], x[1]))[0][1])

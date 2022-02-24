# https://www.acmicpc.net/problem/1032

N = int(input())
files = []
for _ in range(N):
    files.append(input())

###
combined = list(zip(*files))
result = ""

for words_tuple in combined:
    words = sorted(list(words_tuple))
    if words[0] == words[-1]:
        result += words[0]
    else:
        result += "?"

print(result)

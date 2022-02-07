N = int(input())
result = 0
for _ in range(N):
    word = input()
    visited = dict()

    flag = True
    i=0
    while i<len(word):
        if word[i] in visited:
            flag = False
            break
        visited[word[i]] = True
        while i + 1 < len(word) and word[i] == word[i + 1]:
            i += 1
        i+=1

    if flag:
        result += 1

print(result)

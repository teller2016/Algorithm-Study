X = int(input())
woods = [64]

while(sum(woods) > X):
    shortest = woods.pop()
    half = shortest/2
    if(sum(woods) + half) >= X:
        woods.append(half)
    else:
        woods.append(half)
        woods.append(half)

print(len(woods))

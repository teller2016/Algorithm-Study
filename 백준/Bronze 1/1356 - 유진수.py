N = input()

def mul(m:str):
    result = 1
    for num in m:
        result *= int(num)
    return result

def solution(N):
    if len(N) <= 1:
        return False

    for i in range(1, len(N)):
        left = N[:i]
        right = N[i:]
        if mul(left) == mul(right):
            return True

if solution(N):
    print("YES")
else:
    print("NO")


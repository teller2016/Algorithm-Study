def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fac(n, m):
    result = 1
    for _ in range(m):
        result *= n
        n -= 1
    return result


N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    print(fac(b, a) // factorial(a))

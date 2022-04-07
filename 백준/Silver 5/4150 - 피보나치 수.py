import collections


def fibo(n):
    save = collections.defaultdict(int)
    save[1] = 1

    for i in range(2, n + 1):
        save[i] = save[i - 1] + save[i - 2]

    return save[n]


N = int(input())
print(fibo(N))

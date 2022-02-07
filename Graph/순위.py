# https://programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, results):
    record = [[0 for _ in range(n)] for _ in range(n)]

    for a, b in results:
        record[a - 1][b - 1] = 1
        record[b - 1][a - 1] = -1

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if record[i][j] == 1:
                for k in range(n):
                    if record[j][k] == 1:
                        record[i][k] = 1
            elif record[i][j] == -1:
                for k in range(n):
                    if record[j][k] == -1:
                        record[i][k] = -1

    result = 0
    for li in record:
        if li.count(0) == 1:
            result += 1

    print(record)
    return result
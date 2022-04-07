def solution(bingo, call):
    board = [[0]*5 for _ in range(5)]
    result = 0
    for row in call:
        for num in row:
            result += 1
            if num in bingo:
                i,j = bingo[num]
                board[i][j] = 1

                count = 0
                for a in range(5):
                    if sum(board[a]) == 5:
                        count += 1
                    if sum(r[a] for r in board) == 5:
                        count += 1
                if sum(board[a][a] for a in range(5)) == 5:
                    count += 1
                if sum(board[4-a][a] for a in range(5)) == 5:
                    count += 1

                if count >= 3:
                    return result


bingo = dict()
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        bingo[row[j]] = [i,j]


call = []
for _ in range(5):
    row = list(map(int, input().split()))
    call.append(row)

print(solution(bingo, call))
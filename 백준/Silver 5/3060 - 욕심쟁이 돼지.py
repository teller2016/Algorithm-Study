n = int(input())


def solution(total, foods):
    day = 1
    food_total = sum(foods)
    while total >= food_total:
        day += 1
        food_total *= 4

    print(day)


for _ in range(n):
    a = int(input())
    b = list(map(int, input().split()))
    solution(a, b)

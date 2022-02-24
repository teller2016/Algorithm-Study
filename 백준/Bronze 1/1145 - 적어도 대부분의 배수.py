# https://www.acmicpc.net/problem/1145

nums = list(map(int, input().split()))
min_num = min(nums)

while True:
    cnt = 0
    for num in nums:
        if min_num % num == 0:
            cnt += 1

    if cnt >= 3:
        print(min_num)
        break

    min_num += 1

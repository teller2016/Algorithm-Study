# https://programmers.co.kr/learn/courses/30/lessons/43165
# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

def recursive(numbers, index, target):
    if index == len(numbers) and target == 0:
        return 1
    elif index == len(numbers):
        return 0

    return recursive(numbers, index + 1, target + numbers[index]) + recursive(numbers, index + 1,
                                                                              target - numbers[index])


def solution(numbers, target):
    return recursive(numbers, 0, target)

# numbers	target	return
# [1, 1, 1, 1, 1]	3	5

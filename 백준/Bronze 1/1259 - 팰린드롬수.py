# https://www.acmicpc.net/problem/1259

def palindrome1(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def palindrome2(word):
    return word == word[::-1]


while True:
    w = input()
    if w == '0':
        break

    if palindrome2(w):
        print("yes")
    else:
        print("no")

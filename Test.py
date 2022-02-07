def solution(s):
    dic1 = {')':'(', ']':'[', '}':'{'}
    dic2 = {'(':')', '[':']', '{':'}'}
    stack = []
    for i,ch in enumerate(s):
        print(i,ch)



print(solution("[]([[]){}"))
print(solution("{([()]))}"))
print(solution("(()()()"))
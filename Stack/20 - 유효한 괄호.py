# https://leetcode.com/problems/valid-parentheses/submissions/
class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch not in symbol:
                stack.append(ch)
            elif not stack or symbol[ch] != stack.pop():
                return False

        return not stack
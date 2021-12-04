#https://leetcode.com/problems/valid-palindrome/submissions/
# 주어진 문자열이 팰린드롬인지 확인
import collections
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for char in s:
            if char.isalpha() or char.isdigit():
                char = char.lower()
                str.append(char)
        return str == str[::-1]

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        deque = collections.deque()

        for char in s:
            if char.isalnum():
                deque.append(char.lower())

        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False

        return True
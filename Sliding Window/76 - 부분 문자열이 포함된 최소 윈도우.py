# https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]

# 브루트 포스(시간 초과)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def contains(sub, t_list):
            for t_val in t_list:
                if t_val in sub:
                    sub.remove(t_val)
                else:
                    return False
            return True

        window_size = len(t)
        for size in range(window_size, len(s) + 1):
            for i in range(len(s) - window_size + 1):
                sub = s[i:i + size]
                if contains(list(sub), list(t)):
                    return sub

        return ''
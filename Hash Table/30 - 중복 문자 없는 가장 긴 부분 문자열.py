# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

# 내 풀이
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = collections.defaultdict(lambda: 0)
        max_val = 0
        deque = collections.deque()

        for alpha in s:
            if visited[alpha]:
                while deque:
                    left = deque.popleft()
                    visited[left] = 0
                    if alpha == left:
                        break

            deque.append(alpha)
            visited[alpha] = 1
            max_val = max(max_val, len(deque))
        return max_val

# 슬라이딩 윈도우와 투 포인터로 사이즈 조절
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
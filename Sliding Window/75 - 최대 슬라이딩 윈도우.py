# https://leetcode.com/problems/sliding-window-maximum/submissions/

# 큐 이용 (시간 초과)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        result = []
        max_val = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if max_val == float('-inf'):
                max_val = max(window)
            elif v > max_val:
                max_val = v

            result.append(max_val)

            if max_val == window.popleft():
                max_val = float('-inf')

        return result

# 브루트 포스 (시간초과)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))

        return result

# 내풀이 (시간초과)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        result = []
        max_val = float('-inf')
        while nums:
            last = nums.pop()
            window.append(last)
            if len(window) >= k:
                if max_val < last:
                    max_val = max(window)

                result.append(max_val)

                if max_val == window.popleft():
                    max_val = float('-inf')

        return result[::-1]
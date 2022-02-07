#https://leetcode.com/problems/trapping-rain-water/

#투 포인터 이용
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result

# 스택 이용

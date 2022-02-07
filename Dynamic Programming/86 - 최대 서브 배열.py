# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0

        return max(nums)

# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_num = -sys.maxsize
        current_num = 0

        for num in nums:
            current_num = max(num, current_num + num)
            best_num = max(best_num, current_num)
        return best_num
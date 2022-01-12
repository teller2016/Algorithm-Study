# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

# 투 포인터
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] +nums[right] > target:
                right -= 1
            else:
                return left+1, right+1

# 이진 검색
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            tar = target - v

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] < tar:
                    left = mid + 1
                elif nums[mid] > tar:
                    right = mid - 1
                else:
                    return i + 1, mid + 1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):

            tar = target - v
            # sliced = nums[i+1:]  슬라이싱 최소화 가능
            index = bisect.bisect_left(nums[i+1:], tar)
            if len(nums[i+1:])>index and nums[index+i+1] == tar:
                return i+1, i+index+2


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):

            tar = target - v
            index = bisect.bisect_left(nums, tar, i + 1)

            if index < len(nums) and nums[index] == tar:
                return i + 1, index + 1
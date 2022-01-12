# https://leetcode.com/problems/binary-search/

# 재귀
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    return binary_search(left, mid - 1)
                elif target > nums[mid]:
                    return binary_search(mid + 1, right)
                else:
                    return mid

            return -1

        return binary_search(0, len(nums) - 1)

# 반복 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

        return -1

# 이진 모듈 사용
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

#파이썬 방식
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
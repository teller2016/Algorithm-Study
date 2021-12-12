#https://leetcode.com/problems/array-partition-i/submissions/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

# 정렬하고 2개 쌓이면 min구해서 더하기
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        stack = []
        for num in nums:
            stack.append(num)
            if len(stack) == 2:
                result += min(stack)
                stack = []

        return result
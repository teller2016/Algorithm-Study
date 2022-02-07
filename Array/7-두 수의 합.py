#https://leetcode.com/problems/two-sum/submissions/
# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            tar = target - v
            if tar in nums[i+1:]:
                return i, i + 1 + nums[i+1:].index(tar)

# 딕셔너리를 사용해 시간 복잡도 줄임
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, v in enumerate(nums):
            dic[v] = i

        for i, num in enumerate(nums):
            if (target - num) in dic and i != dic[target - num]:
                return i, dic[target - num]
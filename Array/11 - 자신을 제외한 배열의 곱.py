#https://leetcode.com/problems/product-of-array-except-self/submissions/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        front = []
        for i in range(len(nums)):
            front.append(cur)
            cur = cur * nums[i]

        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            front[i] = front[i] * cur
            cur = cur * nums[i]

        return front
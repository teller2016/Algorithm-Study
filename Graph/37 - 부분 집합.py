# https://leetcode.com/problems/subsets/submissions/

# 내 풀이
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def rec(cur, start):
            result.append(cur)
            for i in range(start, len(nums)):
                rec(cur + [nums[i]], i+ 1)

        rec([], 0)

        return result
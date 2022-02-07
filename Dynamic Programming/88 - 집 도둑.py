# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i):
            if i < 0:
                return 0

            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)
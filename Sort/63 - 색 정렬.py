#  https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums ) -1

        while w <= b:
            if nums[w] > 1:
                nums[b], nums[w] = nums[w], nums[b]
                b -= 1
            elif nums[w] < 1:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            else:
                w += 1

        return nums
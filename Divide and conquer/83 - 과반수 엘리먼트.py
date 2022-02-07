# https://leetcode.com/problems/majority-element/submissions/

# 분할 정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]


# DP (메모이제이션) 계산한건 저장해놓기
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num


# 파이썬 풀이
# 과반수(절반 초과를 차지)이면 항상 중앙을 차지한다 + 항상 답이 존재한다는 전제조건
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

# 그냥 가장 많은 숫자 출력
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]
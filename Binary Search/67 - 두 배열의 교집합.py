# https://leetcode.com/problems/intersection-of-two-arrays/

# 브루트 포스
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result

# 이진 검색 이용
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()

        for n1 in nums1:
            i = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i and n1 == nums2[i]:
                result.add(n1)

        return result

# 투 포인터
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        nums1.sort()
        nums2.sort()

        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1

        return result
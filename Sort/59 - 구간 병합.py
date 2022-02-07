# https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        for inter in sorted(intervals, key=lambda x: x[0]):
            if result and result[-1][1] >= inter[0]:
                result[-1][1] = max(result[-1][1], inter[1])
            else:
                result.append(inter)

        return result
# https://leetcode.com/problems/combination-sum/submissions/

# 내 풀이
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def rec(cur, start, t):
            if t== 0:
                result.append(cur[:])
            elif t < 0:
                return

            for i in range(start, len(candidates)):
                cur.append(candidates[i])
                rec(cur, i, t - candidates[i])
                cur.pop()

        rec([], 0, target)

        return result

# 책 풀이
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def rec(cur, start, t):
            if t == 0:
                result.append(cur)
            elif t < 0:
                return

            for i in range(start, len(candidates)):
                rec(cur + [candidates[i]], i, t - candidates[i])

        rec([], 0, target)

        return result
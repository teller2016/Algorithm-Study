# https://leetcode.com/problems/combinations/submissions/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1),k))

# 내 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def rec(cur, remain):
            if len(cur) == k:
                result.append(cur)
                return
            elif len(remain) == 0:
                return

            for i in range(len(remain)):
                temp = cur[:]
                temp.append(remain[i])
                rec(temp, remain[i + 1:])

        rec([], range(1, n + 1))
        return result

# 책 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result
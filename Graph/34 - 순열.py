# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

# dfs 내 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(cur, remain):
            if not remain:
                result.append(cur)
                return

            for i in range(len(remain)):
                temp = cur[:]
                temp.append(remain[i])
                dfs(temp, remain[:i] + remain[i + 1:])

        dfs([], nums)

        return result


# 책 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result
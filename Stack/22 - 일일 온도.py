# https://leetcode.com/problems/daily-temperatures/submissions/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                last = stack.pop()
                result[last] = i - last

            stack.append(i)

        return result
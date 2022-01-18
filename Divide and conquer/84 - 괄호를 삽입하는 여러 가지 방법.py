# https://leetcode.com/problems/different-ways-to-add-parentheses/submissions/

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        def compute(left, right, op):
            result = []
            for l in left:
                for r in right:
                    result.append(eval(str(l) + op + str(r)))

            return result

        if input.isdigit():
            return [int(input)]

        results = []

        for index, value in enumerate(input):
            if value in "+-*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value))

        return results
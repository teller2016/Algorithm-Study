# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

# 내풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2" :"abc" ,"3" :"def" ,"4" :"ghi" ,"5" :"jkl" ,"6" :"mno" ,"7" :"pqrs" ,"8" :"tuv" ,"9" :"wxyz"}
        result = []

        def rec(cur):
            if len(cur) == len(digits):
                result.append(cur)
                return
            for s in dic[digits[len(cur)]]:
                rec(cur + s)

        if not digits:
            return []

        rec('')
        return result

# 책 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        dfs(0, '')

        return result
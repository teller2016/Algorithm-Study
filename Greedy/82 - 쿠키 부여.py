# https://leetcode.com/problems/assign-cookies/submissions/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1

        return result

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = j = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1

        return i
# https://leetcode.com/problems/number-of-1-bits/submissions/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1을 뺀 값과 AND하면 1이 하나씩 없어진다
        count = 0

        while n:
            n &= (n - 1)
            count += 1

        return count
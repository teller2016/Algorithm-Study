# https://leetcode.com/problems/fibonacci-number/

# 타뷸레이션(상향식)
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]

# 메모이제이션(하향식)
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.dp[n]

# 두 정수로 풀이
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1

        for i in range(0, n):
            x, y = x + y, x

        return x

# 브루트 포스
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

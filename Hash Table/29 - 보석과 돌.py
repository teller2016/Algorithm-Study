# https://leetcode.com/problems/jewels-and-stones/submissions/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = collections.Counter(stones)
        return sum([stone_count[jewel] for jewel in jewels])

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
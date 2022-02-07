# https://leetcode.com/problems/top-k-frequent-elements/submissions/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        return list(zip(*freq.most_common(k)))[0]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        Q = []

        for key in freq:
            heapq.heappush(Q, (-freq[key], key))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(Q)[1])
        return result
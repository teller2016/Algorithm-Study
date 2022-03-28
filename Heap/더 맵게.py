# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    result = 0

    heapq.heapify(scoville)
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K:
            break

        heapq.heappush(scoville, first + second * 2)
        result += 1

    if len(scoville) == 1:
        first = heapq.heappop(scoville)
        if first < K:
            return -1

    return result
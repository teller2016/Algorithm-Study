# https://programmers.co.kr/learn/courses/30/lessons/43163
# begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
# 최소 거리를 구하는 것이므로 BFS 사용
import collections


def getSimilar(cur, words):
    result = []
    for word in words:
        if sum([0 if a == b else 1 for a, b in zip(cur, word)]) == 1:
            result.append(word)
    return result


def solution(begin, target, words):
    if target not in words:
        return 0

    Q = collections.deque()
    Q.append([begin, words, 0])

    while Q:
        cur, cur_words, cnt = Q.popleft()

        if cur == target:
            return cnt

        similars = getSimilar(cur, cur_words)

        for similar in similars:
            new_words = cur_words[:]
            new_words.remove(similar)
            Q.append([similar, new_words, cnt + 1])

    return 0

# begin	target	words	return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0

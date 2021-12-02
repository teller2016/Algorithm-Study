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
        similars = getSimilar(cur, cur_words)
        print(similars)

    return 0

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
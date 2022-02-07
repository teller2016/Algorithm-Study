#https://programmers.co.kr/learn/courses/30/lessons/43164
#항상 "ICN" 공항에서 출발합니다.
#항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

import collections

def dfs(dic, N, cur, footprint):
    if N == len(footprint):
        return footprint

    for i, dest in enumerate(dic[cur]):
        save = dic[cur]
        dic[cur] = dic[cur][:i] + dic[cur][i + 1:]
        result = dfs(dic, N, dest, footprint + [dest])
        dic[cur] = save

        if result:
            return result


def solution(tickets):
    tickets.sort(key=lambda x: x[1])
    dic = collections.defaultdict(list)
    for src, dst in tickets:
        dic[src].append(dst)
    N = len(tickets) + 1
    return dfs(dic, N, "ICN", ["ICN"])

#tickets	return
#[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
#[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# https://leetcode.com/problems/reconstruct-itinerary/submissions/

#################################다시 풀어보기########################################

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        result = []

        def dfs(cur):
            while graph[cur]:
                dfs(graph[cur].pop())
            result.append(cur)

        dfs("JFK")
        return result[::-1]
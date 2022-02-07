graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def recursive_dfs(cur, discovered=[]):
    global graph
    discovered.append(cur)
    for num in graph[cur]:
        if num not in discovered:
            discovered = recursive_dfs(num, discovered)
    return discovered

def stack_dfs(cur):
    global graph
    stack = [cur]
    discovered = []
    while stack:
        last = stack.pop()
        if last not in discovered:
            discovered.append(last)
            for num in graph[last]:
                stack.append(num)

    return discovered

# 내 풀이
def bfs(cur):
    global graph
    queue = [cur]
    discovered = []

    while queue:
        last = queue.pop(0)
        if last not in discovered:
            discovered.append(last)
            for num in graph[last]:
                queue.append(num)

    return discovered

# 책 풀이
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)		# deqeue를 사용하면 성능이 높아진다
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered

print(recursive_dfs(1))
print(stack_dfs(1))
print(bfs(1))
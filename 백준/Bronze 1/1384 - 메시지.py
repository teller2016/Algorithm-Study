import collections

repeat = 1
while True:
    N = int(input())
    if N == 0:
        break

    data = collections.deque()
    for _ in range(N):
        data.appendleft(input())

    result = []
    for _ in range(len(data)):
        paper = data[0].split()

        NP = paper[1:]
        result_temp = []
        for i, np in enumerate(NP):
            if np == 'N':
                note = data[i + 1].split()[0] + " was nasty about " + paper[0]
                result_temp.append(note)

        result = result_temp + result
        data.append(data.popleft())

    print("Group " + str(repeat))
    repeat += 1

    if len(result) == 0:
        print("Nobody was nasty")
    else:
        for note in result:
            print(note)
    print()

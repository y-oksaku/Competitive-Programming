B = [list(map(int, input().split())) for _ in range(2)]
C = [list(map(int, input().split())) for _ in range(3)]

minMemo = {}
maxMemo = {}
def search(chart, player):
    for i in range(3):
        for j in range(3):
            if chart[i * 3 + j] == -1:
                break
        else:
            continue
        break
    else:
        ret = [0, 0]
        for i in range(2):
            for j in range(3):
                if chart[i * 3 + j] == chart[(i + 1) * 3 + j]:
                    ret[0] += B[i][j]
                else:
                    ret[1] += B[i][j]
        for i in range(3):
            for j in range(2):
                if chart[i * 3 + j] == chart[i * 3 + (j + 1)]:
                    ret[0] += C[i][j]
                else:
                    ret[1] += C[i][j]
        return ret

    if player == 0:  # max
        if tuple(chart) in maxMemo:
            return maxMemo[tuple(chart)]

        ret = [-float('inf'), 0]
        for i in range(3):
            for j in range(3):
                if chart[i * 3 + j] == -1:
                    d = chart.copy()
                    d[i * 3 + j] = 0
                    e = search(d, 1)
                    if ret[0] < e[0]:
                        ret = e
        maxMemo[tuple(chart)] = ret
    else:
        if tuple(chart) in minMemo:
            return minMemo[tuple(chart)]

        ret = [0, -float('inf')]
        for i in range(3):
            for j in range(3):
                if chart[i * 3 + j] == -1:
                    d = chart.copy()
                    d[i * 3 + j] = 1
                    e = search(d, 0)
                    if ret[1] < e[1]:
                        ret = e
        minMemo[tuple(chart)] = ret
    return ret

chart = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
ans = search(chart, 0)
print(ans[0])
print(ans[1])
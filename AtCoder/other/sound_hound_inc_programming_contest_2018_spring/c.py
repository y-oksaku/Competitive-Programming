R, C = map(int, input().split())
chart = [input().rstrip() for _ in range(R)]
N = R * C

edge = [[] for _ in range(N)]

for r in range(R):
    for c in range(C - 1):
        if not (chart[r][c] == chart[r][c + 1] == '.'):
            continue
        n = r * C + c
        edge[n].append(n + 1)
        edge[n + 1].append(n)

for c in range(C):
    for r in range(R - 1):
        if not (chart[r][c] == chart[r + 1][c] == '.'):
            continue
        n = r * C + c
        edge[n].append(n + C)
        edge[n + C].append(n)

count = sum([s.count('.') for s in chart])
match = [-1] * N
used = [False] * N

def dfs(v):
    used[v] = True
    for to in edge[v]:
        w = match[to]
        if w < 0 or (not used[w] and dfs(w)):
            match[v] = to
            match[to] = v
            return True
    return False

def matching():
    global used
    ret = 0
    for v in range(N):
        if match[v] < 0:
            used = [False] * N
            if dfs(v):
                ret += 1
    return ret

print(count - matching())

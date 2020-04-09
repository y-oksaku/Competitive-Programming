from itertools import permutations

N, M = map(int, input().split())
edges = [set() for _ in range(N)]

for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].add(to)
    edges[to].add(fr)

def existsPath(path):
    for fr, to in zip(path, path[1:]):
        if not to in  edges[fr]:
            return False
    return True

ans = 0
for path in permutations(range(1, N), r=N-1):
    if existsPath((0,) + path):
        ans += 1
print(ans)

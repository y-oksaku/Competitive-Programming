from itertools import permutations

N, M = map(int, input().split())

edges =[set() for _ in range(N)]
for _ in range(M):
    fr, to = map(int, input().split())
    fr -= 1
    to -= 1
    edges[fr].add(to)
    edges[to].add(fr)

ans = 0
for perm in permutations(range(1, N), r=N-1):
    for prev, now in zip((0,) + perm, perm):
        if not now in edges[prev]:
            break
    else:
        ans += 1

print(ans)

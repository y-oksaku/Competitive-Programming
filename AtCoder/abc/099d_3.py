from itertools import permutations

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]

cnt = [[0] * C for _ in range(3)]
for h in range(N):
    for w, c in enumerate(map(int, input().split())):
        cnt[(h + w) % 3][c - 1] += 1

ans = 10**18
for perm in permutations(range(C), r=3):
    cost = 0
    for c, ns in zip(perm, cnt):
        for fr in range(C):
            if fr == c:
                continue
            cost += D[fr][c] * ns[fr]
    ans = min(ans, cost)
print(ans)
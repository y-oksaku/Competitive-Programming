N, M, X = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

def calc(state):
    ret = 0
    S = [0] * M
    for i, B in enumerate(A):
        if ((1 << i) & state) == 0:
            continue
        for j, a in enumerate(B[1:]):
            S[j] += a
        ret += B[0]
    if all(s >= X for s in S):
        return ret
    return 10**18

ans = 10**18
for state in range(1 << N):
    ans = min(ans, calc(state))

print(ans if ans < 10**18 else -1)

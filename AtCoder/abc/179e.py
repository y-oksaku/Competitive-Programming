N, X, M = map(int, input().split())

isUsed = [False] * M
isUsed[X] = True
S = [X]
st = X
while True:
    nx = X**2 % M
    if isUsed[nx]:
        st = nx
        break
    isUsed[nx] = True
    S.append(nx)
    X = nx

idx = S.index(st)
L, R = S[:idx], S[idx:]

ans = sum(L[:N])
N = max(0, N - len(L))

q, r = divmod(N, len(R))
ans += q * sum(R) + sum(R[:r])

print(ans)
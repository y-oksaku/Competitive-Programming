N, K = map(int, input().split())
coins = []

for _ in range(N):
    A, B = map(int, input().split())
    coins.append((A, B + 1))

def isOk(m):
    cnt = 0
    for a, b in coins:
        if a >= m:
            continue
        cnt += min(m, b) - a
    return cnt < K

ok = 0
ng = 10**9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)
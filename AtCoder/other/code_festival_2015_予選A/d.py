N, M = map(int, input().split())
X = [int(input()) for _ in range(M)]

def isOk(T):
    R = 1
    for x in X:
        L = max(0, x - R)
        if L > T:
            return False
        if L == 0:
            R = x + T + 1
        else:
            D = max(0, T - L * 2)
            R = max(x + (T - L) // 2 + 1, x + D + 1)
    return N < R

ok = 10**10
ng = -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)

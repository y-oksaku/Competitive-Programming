N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

def isOk(n):
    if n < P:
        return True
    b = A[n] + M

    cnt = (P - 1) * M + (N - n) * M
    for a in A[P - 1: n]:
        cnt += max(0, b - a)

    if b >= A[P - 1] and cnt >= V * M:
        return True
    return False

ok = -1
ng = N
while ng - ok > 1:
    mid = (ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ng)
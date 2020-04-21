N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)

def isOk(i):
    if i < P:
        return True

    b = A[i] + M
    if b < A[P - 1]:
        return False

    cnt = (P - 1) * M + (N - i) * M

    for a in A[P - 1: i]:
        cnt += max(0, b - a)
    return cnt >= M * V

ok = 0
ng = N
while ng - ok > 1:
    mid = (ng + ok) // 2

    if isOk(mid):
        ok = mid
    else:
        ng = mid
print(ng)


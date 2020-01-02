N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
W = N - V

def isOk(n):
    if n < P:
        return True
    b = A[n]

    D = [max(0, a - b) for a in A][P - 1:]
    cnt = -(-(sum(D) - W) // W) + 1

    return max(max(D), cnt) <= M

ok = -1
ng = N
while ng - ok > 1:
    mid = (ng + ok) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ng)
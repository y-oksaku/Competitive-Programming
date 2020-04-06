N, M, V, P = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

def isOk(i):
    x = A[i] + M
    B = [x - a for a in A[P - 1: i]]

    if not B:
        return True
    cnt = sum(B) + (P - 1) * M + (N - i) * M
    return min(B) >= 0 and cnt >= M * V

ok = 0
ng = N
while ng - ok > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
print(ng)

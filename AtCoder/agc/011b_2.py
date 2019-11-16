N = int(input())
A = list(map(int, input().split()))
A.sort()

def isOk(n):
    now = sum(A[:n + 1])
    for a in A[n + 1:]:
        if a <= now * 2:
            now += a
        else:
            return False
    return True

ok = N - 1
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2

    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(N - (ng + 1))
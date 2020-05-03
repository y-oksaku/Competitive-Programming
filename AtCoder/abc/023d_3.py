N = int(input())
HS = [tuple(map(int, input().split())) for _ in range(N)]

def isOk(X):
    for i, t in enumerate(sorted([(X - h) // s for h, s in HS])):
        if i > t:
            return False
    return True

ok = 10**18
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid
print(ok)

import sys
input = sys.stdin.buffer.readline

N = int(input())
HS = [tuple(map(int, input().split())) for _ in range(N)]

ok = 10**18
ng = 0

def isOk(K):
    for i, b in enumerate(sorted([(K - h) // s for h, s in HS])):
        if i > b:
            return False
    return True

while ok - ng > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)

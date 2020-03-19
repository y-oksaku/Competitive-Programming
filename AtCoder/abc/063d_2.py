import sys
input = sys.stdin.buffer.readline

N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]

ok = 10**18
ng = 0

def isOk(n):
    cnt = 0
    for h in H:
        h -= B * n
        if h > 0:
            cnt += -(-h // (A - B))
    return cnt <= n

while ok - ng > 1:
    mid = (ok + ng) // 2
    if isOk(mid):
        ok = mid
    else:
        ng = mid

print(ok)
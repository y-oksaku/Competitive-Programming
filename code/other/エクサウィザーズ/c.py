N, Q = map(int, input().split())
S = input()

query = []

for _ in range(Q):
    t, d = input().split()
    query.append((t, d))

def isDropLeft(i):
    now = i

    for t, d in query:
        if S[now] == t:
            if d == 'L':
                now -= 1
            else:
                now += 1
        if now < 0:
            return True
        if now >= N:
            return False
    return False

def isDropRight(i):
    now = i

    for t, d in query:
        if S[now] == t:
            if d == 'L':
                now -= 1
            else:
                now += 1
        if now < 0:
            return False
        if now >= N:
            return True
    return False

okLeft = -1
ngLeft = N

while ngLeft - okLeft > 1:
    mid = (okLeft + ngLeft) // 2
    if isDropLeft(mid):
        okLeft = mid
    else:
        ngLeft = mid

okRight = N
ngRight = -1

while okRight - ngRight > 1:
    mid = (okRight + ngRight) // 2
    if isDropRight(mid):
        okRight = mid
    else:
        ngRight = mid

ans = N - ((okLeft + 1) + (N - okRight))
print(ans)
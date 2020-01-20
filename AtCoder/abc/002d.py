N, M = map(int, input().split())
friends = [set() for _ in range(N)]

for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    friends[X].add(Y)
    friends[Y].add(X)

def canMake(mask):
    for fr in range(N):
        for to in range(fr + 1, N):
            if ((1 << fr) & mask) > 0 and ((1 << to) & mask) > 0:
                if not to in friends[fr]:
                    return False
    return True

ans = 1
for mask in range(1 << N):
    if canMake(mask):
        cnt = 0
        for d in range(N):
            if ((1 << d) & mask) > 0:
                cnt += 1
        ans = max(ans, cnt)
print(ans)